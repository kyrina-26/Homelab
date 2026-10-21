# Readest Sync — Modified Calibre Plugin

An unofficial modified version of the Readest Calibre plugin for synchronizing Calibre books and metadata with Readest.

## Based on

This project is based on the official Readest project:

- **Project:** [Readest](https://github.com/readest/readest)
- **License:** GNU Affero General Public License v3 or later (AGPL-3.0-or-later)
- **Upstream plugin version:** 0.12.16

## Modifications

This version includes the following changes:

- Added configuration fields for the self-hosted Readest API URL, Supabase URL, and Supabase anon key.
- Improved matching of Calibre books using their UUIDs in Readest metadata.
- Added automatic pushing of replacement EPUBs to Readest, allowing chapter updates from FanFicFare to sync with existing books. **Metadata updates still require a manual push**, as in the standard Readest plugin.
- Added automatic book imports into Readest, removing the need to use OPDS for importing books. **Warning:** Using this modified plugin alongside OPDS may cause duplicate-book errors.

## Distribution contents

- `readest-sync-0.12.16.calibre-plugin` — installable Calibre plugin.
- `src/` — plugin source code.
- `LICENSE` — license text.

## Installation

In Calibre, open **Preferences → Plugins → Load plugin from file**, select the `.calibre-plugin` file, and restart Calibre if prompted.

Configure the API and Supabase settings in the plugin preferences as appropriate for your Readest deployment.

## License and attribution

This project contains code from the Readest project and includes modifications. The applicable license and upstream copyright notices are provided in `LICENSE` and the source files.

This is an unofficial modified project and is not an official Readest release. Readest's original authors retain their respective copyrights.

## Source

The complete source code for this distribution is included in `src/`.

