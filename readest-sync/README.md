# Readest Sync — Modified Calibre Plugin

An unofficial modified version of the Readest Calibre plugin for synchronizing Calibre books and metadata with Readest.

## Upstream Project

- **Project:** [Readest](https://github.com/readest/readest)
- **License:** GNU Affero General Public License v3 or later (AGPL-3.0-or-later)
- **Upstream plugin version:** 0.12.16

## Modifications

This version includes the following changes:

- Added configuration fields for the self-hosted Readest API URL, Supabase URL, and Supabase anon key.
- Improved matching of Calibre books using their UUIDs in Readest metadata.
- Added automatic pushing of replacement EPUBs to Readest, allowing chapter updates from FanficFare to sync with existing books. **Metadata updates still require a manual push**, as in the standard Readest plugin.
- Added automatic book imports into Readest, removing the need to use OPDS for importing books. **Automatic imports are supported only for books added through FanficFare.** Books added through Calibre's built-in **Add books** function are not automatically imported and must be pushed to Readest manually. **Warning:** Using this modified plugin alongside OPDS may cause duplicate-book errors.

## Files

- `readest-sync-0.12.16.zip` — installable Calibre plugin archive.
- `src/` — plugin source code.
- `LICENSE` — license text.

## Installation

1. Download `readest-sync-0.12.16.zip` from this repository.
2. Place the archive in the `plugins-install` folder accessible through your network share.
3. Open Calibre and navigate to **Preferences → Plugins**.
4. Select **Load plugin from file**.
5. Browse to `/config/plugins-install/`, select `readest-sync-0.12.16.zip`, and confirm the installation.
6. Restart Calibre if prompted.

Configure the API and Supabase settings in the plugin preferences as appropriate for your Readest deployment.

## License and Attribution

This project contains code from the Readest project and includes modifications. The applicable license and upstream copyright notices are provided in `LICENSE` and the source files.

This is an unofficial modified project and is not an official Readest release. Readest's original authors retain their respective copyrights.

The complete source code for this distribution is included in `src/`.
