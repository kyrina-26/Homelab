# Local modifications documented 2026-10-20:
# Updated Readest Sync UI/client handling for configured self-hosted
# endpoints, authentication state, and custom-column preferences.
# Original copyright and license notices remain applicable.

__license__ = 'AGPL v3'
__copyright__ = '2026, Bilingify LLC'

from datetime import datetime
from pathlib import Path

from qt.core import QMenu, QTimer, pyqtSignal
from calibre.db.cache import EventType

from calibre.gui2 import error_dialog, info_dialog
from calibre.gui2.actions import InterfaceAction

from calibre_plugins.readest.api import ReadestClient
from calibre_plugins.readest.config import prefs, save_tokens
from calibre_plugins.readest.dialogs import LoginDialog, PushDialog, StatusDialog
from calibre_plugins.readest.wire import merge_marks
from calibre_plugins.readest.worker import PushWorker

try:
    load_translations()
except NameError:
    pass


def make_client():
    return ReadestClient(
        api_base=prefs['api_base'],
        supabase_url=prefs['supabase_url'],
        anon_key=prefs['anon_key'],
        tokens=prefs['tokens'],
        on_tokens=save_tokens,
    )


class ReadestInterfacePlugin(InterfaceAction):
    _auto_push_signal = pyqtSignal(int)
    name = 'Readest Sync'
    action_spec = (
        _('Readest'),
        None,
        _('Push selected books and metadata to your Readest library'),
        None,
    )

    def genesis(self):
        self.push_action = self.create_action(
            spec=(_('Push selected books to Readest'), None, None, None),
            attr='Push selected books to Readest',
        )
        self.push_action.triggered.connect(self.push_selected)

        self.check_action = self.create_action(
            spec=(_('Check Readest status'), None, None, None),
            attr='Check Readest status of selected books',
        )
        self.check_action.triggered.connect(self.check_selected)

        self.login_action = self.create_action(
            spec=(_('Log in to Readest…'), None, None, None), attr='Log in to Readest'
        )
        self.login_action.triggered.connect(self.login)

        self.logout_action = self.create_action(
            spec=(_('Log out'), None, None, None), attr='Log out from Readest'
        )
        self.logout_action.triggered.connect(self.logout)

        self.config_action = self.create_action(
            spec=(_('Customize plugin…'), None, None, None), attr='Customize Readest plugin'
        )
        self.config_action.triggered.connect(self.show_config)

        self.menu = QMenu(self.gui)
        self.menu.addAction(self.push_action)
        self.menu.addAction(self.check_action)
        self.menu.addSeparator()
        self.menu.addAction(self.login_action)
        self.menu.addAction(self.logout_action)
        self.menu.addAction(self.config_action)
        self.menu.aboutToShow.connect(self.update_menu)

        self.qaction.setMenu(self.menu)
        self.qaction.setIcon(get_icons('images/icon.png', 'Readest Sync'))
        self.qaction.triggered.connect(self.push_selected)
        self._event_db = None
        self._auto_push_signal.connect(self._schedule_auto_push)
        self._recent_epub_removals = {}
        self._auto_timers = {}
        self._auto_queue = []
        self._auto_worker = None

    def update_menu(self):
        logged_in = bool(prefs['tokens'])
        email = prefs['user_email']
        self.login_action.setVisible(not logged_in)
        self.logout_action.setVisible(logged_in)
        if logged_in and email:
            self.logout_action.setText(_('Log out (%s)') % email)
        selected = len(self.selected_book_ids()) > 0
        self.push_action.setEnabled(selected)
        self.check_action.setEnabled(selected)

    def initialization_complete(self):
        self._attach_event_listener()

    def library_about_to_change(self, *args, **kwargs):
        self._detach_event_listener()

    def library_changed(self, *args, **kwargs):
        self._attach_event_listener()

    def _write_event_log(self, message):
        return

    def _attach_event_listener(self):
        try:
            db = self.gui.current_db.new_api
            dispatcher = getattr(db, 'event_dispatcher', None)
            self._write_event_log(
                'DB type=%r dispatcher=%r dispatcher_type=%r methods=%r'
                % (
                    type(db), dispatcher, type(dispatcher),
                    [n for n in dir(dispatcher) if 'event' in n.lower() or 'listener' in n.lower()]
                    if dispatcher is not None else [],
                )
            )
            if db is self._event_db:
                return
            self._detach_event_listener()
            self._event_callback = self._on_db_event
            db.add_listener(self._event_callback, check_already_added=True)
            self._event_db = db
            self._write_event_log('Listener attached')
        except Exception as err:
            self._write_event_log('Listener attach failed: %r' % (err,))

    def _detach_event_listener(self):
        db, self._event_db = self._event_db, None
        if db is not None:
            try:
                db.remove_listener(self._event_callback)
                self._write_event_log('Listener detached')
            except Exception as err:
                self._write_event_log('Listener detach failed: %r' % (err,))

    def _on_db_event(self, event_type, library_id, event_data):
        # Keep diagnostic event logging while testing the trigger.
        self._write_event_log(
            'database_event type=%r library_id=%r event_data=%r'
            % (event_type, library_id, event_data)
        )

        now = datetime.now().timestamp()

        # Remember removal of an EPUB belonging to an existing book.
        if event_type == EventType.formats_removed:
            try:
                removed = event_data[0]
                for book_id, formats in removed.items():
                    if 'EPUB' in formats:
                        self._recent_epub_removals[book_id] = now
                        self._write_event_log(
                            'Candidate EPUB replacement book_id=%r' % book_id
                        )
            except Exception as err:
                self._write_event_log(
                    'Could not inspect formats_removed event: %r' % err
                )
            return

        if event_type != EventType.format_added:
            return

        try:
            book_id, fmt = event_data
        except (TypeError, ValueError):
            return

        if fmt != 'EPUB':
            return

        removed_at = self._recent_epub_removals.pop(book_id, None)
        if removed_at is None or now - removed_at > 120:
            return

        self._write_event_log(
            'Replacement EPUB detected for book_id=%r; waiting 5 seconds'
            % book_id
        )

        # Hand timer creation to the plugin's Qt thread.
        self._auto_push_signal.emit(book_id)

    def _schedule_auto_push(self, book_id):
        timer = self._auto_timers.get(book_id)
        if timer is None:
            timer = QTimer(self)
            timer.setSingleShot(True)
            timer.timeout.connect(
                lambda bid=book_id: self._auto_push_timer_fired(bid)
            )
            self._auto_timers[book_id] = timer
        timer.start(5000)
        self._write_event_log(
            'Replacement timer scheduled on Qt thread for book_id=%r'
            % book_id
        )

    def _auto_push_timer_fired(self, book_id):
        self._auto_timers.pop(book_id, None)

        if not prefs['tokens']:
            self._write_event_log(
                'Automatic push skipped for book_id=%r: not logged in'
                % book_id
            )
            return

        if book_id not in self._auto_queue:
            self._auto_queue.append(book_id)
        self._write_event_log(
            'Automatic push queued for book_id=%r' % book_id
        )
        self._start_next_auto_push()

    def _start_next_auto_push(self):
        if self._auto_worker is not None or not self._auto_queue:
            return

        book_id = self._auto_queue.pop(0)

        try:
            db = self.gui.current_db.new_api
            worker = PushWorker(
                self,
                db,
                [book_id],
                make_client(),
                bool(prefs['include_custom_columns']),
            )
            self._auto_worker = worker
            worker.book_status.connect(self._auto_book_status)
            worker.done.connect(self._auto_push_finished)
            worker.finished.connect(worker.deleteLater)

            self._write_event_log(
                'Automatic push starting for book_id=%r' % book_id
            )
            worker.start()
        except Exception as err:
            self._auto_worker = None
            self._write_event_log(
                'Could not start automatic push for book_id=%r: %r'
                % (book_id, err)
            )
            self._start_next_auto_push()

    def _auto_book_status(self, book_id, status, detail):
        self._write_event_log(
            'Automatic push result book_id=%r status=%r detail=%r'
            % (book_id, status, detail)
        )

    def _auto_push_finished(self, success, message):
        self._write_event_log(
            'Automatic push finished success=%r message=%r'
            % (success, message)
        )
        self._auto_worker = None
        self._start_next_auto_push()

    def selected_book_ids(self):
        return self.gui.library_view.get_selected_ids()

    def push_selected(self):
        self.run_on_selection(PushDialog, _('Select the books to push to Readest.'))

    def check_selected(self):
        self.run_on_selection(StatusDialog, _('Select the books to check against Readest.'))

    def run_on_selection(self, dialog_class, no_selection_message):
        book_ids = self.selected_book_ids()
        if not book_ids:
            return error_dialog(
                self.gui, _('No books selected'), no_selection_message, show=True
            )
        if not prefs['tokens'] and not self.login():
            return
        dialog = dialog_class(
            self.gui,
            self.gui.current_db.new_api,
            book_ids,
            make_client(),
            bool(prefs['include_custom_columns']),
        )
        dialog.exec()
        self.apply_marks(dialog.marks)

    def apply_marks(self, marks):
        """Show the result in the book list as calibre marks (`marked:readest_*`)."""
        if not marks:
            return
        view = self.gui.current_db.data
        # Repaint the rows we are marking plus the ones we are unmarking.
        touched = set(view.marked_ids) | set(marks)
        view.set_marked_ids(merge_marks(view.marked_ids, marks))
        self.gui.library_view.model().refresh_ids(sorted(touched))

    def login(self):
        dialog = LoginDialog(self.gui, make_client())
        if dialog.exec() != dialog.DialogCode.Accepted:
            return False
        user = dialog.user or {}
        prefs['user_email'] = user.get('email')
        info_dialog(
            self.gui,
            _('Readest'),
            _('Logged in as %s.') % (user.get('email') or _('your Readest account')),
            show=True,
        )
        return True

    def logout(self):
        try:
            make_client().sign_out()
        finally:
            save_tokens(None)

    def show_config(self):
        self.interface_action_base_plugin.do_user_config(self.gui)
