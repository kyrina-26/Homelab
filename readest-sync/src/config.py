# Local modifications documented 2026-10-20:
# Added self-hosted API/Supabase configuration, anon-key settings,
# and the custom-columns preference.
# Original copyright and license notices remain applicable.

__license__ = 'AGPL v3'
__copyright__ = '2026, Bilingify LLC'

from calibre.utils.config import JSONConfig
from qt.core import QCheckBox, QLabel, QLineEdit, QVBoxLayout, QWidget

from calibre_plugins.readest.api import (
    DEFAULT_API_BASE,
    DEFAULT_SUPABASE_URL,
    DEFAULT_ANON_KEY,
)

prefs = JSONConfig('plugins/readest')

prefs.defaults['api_base'] = DEFAULT_API_BASE
prefs.defaults['supabase_url'] = DEFAULT_SUPABASE_URL
prefs.defaults['anon_key'] = DEFAULT_ANON_KEY
prefs.defaults['tokens'] = None
prefs.defaults['user_email'] = None
prefs.defaults['include_custom_columns'] = True


def save_tokens(tokens):
    prefs['tokens'] = tokens
    if tokens is None:
        prefs['user_email'] = None


class ConfigWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.l = QVBoxLayout()
        self.setLayout(self.l)

        self.l.addWidget(QLabel('API server:'))
        self.api_base_edit = QLineEdit(self)
        self.api_base_edit.setText(prefs['api_base'])
        self.api_base_edit.setToolTip(
            'Only change this if you run a self-hosted Readest server.'
        )
        self.l.addWidget(self.api_base_edit)

        self.l.addWidget(QLabel('Supabase URL:'))
        self.supabase_url_edit = QLineEdit(self)
        self.supabase_url_edit.setText(prefs['supabase_url'])
        self.l.addWidget(self.supabase_url_edit)

        self.l.addWidget(QLabel('Supabase anon key:'))
        self.anon_key_edit = QLineEdit(self)
        self.anon_key_edit.setText(prefs['anon_key'])
        self.l.addWidget(self.anon_key_edit)

        self.custom_columns_checkbox = QCheckBox(
            'Include custom columns'
        )
        self.custom_columns_checkbox.setChecked(
            prefs['include_custom_columns']
        )
        self.l.addWidget(self.custom_columns_checkbox)

        self.l.addStretch(1)

    def save_settings(self):
        prefs['include_custom_columns'] = (
            self.custom_columns_checkbox.isChecked()
        )
        prefs['api_base'] = (
            self.api_base_edit.text().strip() or DEFAULT_API_BASE
        )
        prefs['supabase_url'] = (
            self.supabase_url_edit.text().strip() or DEFAULT_SUPABASE_URL
        )
        prefs['anon_key'] = (
            self.anon_key_edit.text().strip() or DEFAULT_ANON_KEY
        )
