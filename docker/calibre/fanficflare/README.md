# FanFicFare — FlareSolverr Adapter Archive

This directory preserves the FanFicFare Calibre plugin ZIP and the Wattpad adapter used by my Calibre and FlareSolverr setup.

## Files

- `FanFicFare-4.61.9.zip` — preserved copy of the FanFicFare Calibre plugin, based on upstream version 4.61.9, with a local Wattpad compatibility modification.
- `adapter_wattpadcom.py` — separate copy of the modified Wattpad adapter for reference and preservation.
- `src/` — extracted source files from the plugin ZIP, including the local Wattpad adapter modification.
- `LICENSE` — license text obtained from the official FanFicFare GitHub repository.

## Wattpad / FlareSolverr compatibility

The Wattpad adapter includes handling for FlareSolverr v2 responses in which API HTML is wrapped in a browser `<pre>` element. The modification extracts and HTML-decodes the original chapter content.

A modification notice is included in the relevant adapter files. Original upstream copyright and license notices are retained.

## Upstream project

FanFicFare: https://github.com/JimmXinu/FanFicFare

FanFicFare is developed and maintained by its upstream contributors. This archive preserves the plugin and documents local compatibility changes for reference and future installation.

## Licensing

Consult `LICENSE` for the upstream license terms. The FanFicFare repository identifies the main FanFicFare code under the Apache License 2.0 and its Calibre plugin code under GNU GPL v3.

When redistributing the plugin or source files, retain applicable copyright and license notices and comply with the terms of the relevant licenses. Bundled dependencies may have their own license terms; consult the notices included with the plugin archive.
