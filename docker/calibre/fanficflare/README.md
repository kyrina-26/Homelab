# FanFicFare — Modified Calibre Plugin

An unofficial modified version of the FanFicFare Calibre plugin with a Wattpad compatibility modification for use with FlareSolverr.

## Upstream Project

- **Project:** [FanFicFare](https://github.com/JimmXinu/FanFicFare)
- **Upstream plugin version:** 4.61.9
- **Licensing:** The upstream repository identifies the main FanFicFare code under the Apache License 2.0 and its Calibre plugin code under GNU GPL v3.

## Modifications

This version includes the following change:

- Modified the Wattpad adapter to handle FlareSolverr v2 responses in which API HTML is wrapped in a browser `<pre>` element. The modification extracts and HTML-decodes the original chapter content.

A modification notice is included in the relevant adapter files. Original upstream copyright and license notices are retained.

## Distribution Contents

- `FanFicFare-4.61.9.zip` — installable Calibre plugin archive with the Wattpad compatibility modification.
- `adapter_wattpadcom.py` — separate copy of the modified Wattpad adapter for reference and preservation.
- `src/` — extracted source files from the plugin archive, including the modified Wattpad adapter.
- `personal.ini.example` — sample FanFicFare personal configuration demonstrating site-specific settings, including Wattpad FlareSolverr integration and metadata replacements. Credentials are represented by placeholders.
- `LICENSE` — license text obtained from the official FanFicFare GitHub repository.

## Installation

1. Download `FanFicFare-4.61.9.zip` from this repository.
2. Place the archive in the `plugins-install` folder accessible through your network share.
3. Open Calibre and navigate to **Preferences → Plugins**.
4. Select **Load plugin from file**.
5. Browse to `/config/plugins-install/`, select `FanFicFare-4.61.9.zip`, and confirm the installation.
6. Restart Calibre if prompted.
7. To apply the sample configuration, open **Preferences → Plugins**, select **FanFicFare**, and choose **Customize plugin → Personal.ini** (the wording may vary slightly by version).
8. Select the existing contents of the personal INI and replace them with the contents of `personal.ini.example` from this repository.
9. Replace the placeholder usernames and passwords with your own credentials for the relevant websites. You can add credentials for other supported sites as needed.
10. Save the configuration and confirm that the settings are applied.

**Note:** Replacing the existing personal INI will overwrite its current contents. Back it up first if you want to keep your existing settings.

## License and Attribution

This project contains code from the FanFicFare project and includes a local modification. The applicable license and upstream copyright notices are provided in `LICENSE` and the source files.

FanFicFare is developed and maintained by its upstream contributors. This is an unofficial modified project and is not an official FanFicFare release.

The FanFicFare repository identifies the main FanFicFare code under the Apache License 2.0 and its Calibre plugin code under GNU GPL v3. Retain applicable copyright and license notices when redistributing the plugin or source files and comply with the terms of the relevant licenses. Bundled dependencies may have their own license terms; consult the notices included with the plugin archive.
