# Cutset wordmark and app icons

[cutset-wordmark.svg](cutset-wordmark.svg) is the editable lettering master.
Its six paths trace the approved ImageGen artwork. The lowercase letters are
violet (`#673B99`) with a single golden yellow `s` (`#ECAA1E`). The horizontal
SVG has a transparent background and a viewBox of 76 165 1831 470. A 512 px
wide transparent [PNG](cutset-wordmark.png) is available for raster controls.

The square desktop icon stacks the original `cut` and `set` outlines on a white
tile. Icons smaller than 32 px (32 pt on macOS) and the browser favicon use the purple `c` and
golden yellow `s`. The nightly channel has a lavender tile and an underline.
macOS versions center the tile within the system icon grid. Historical filenames
are retained where the existing Rust and package entry points reference them.

Run `bash packaging/icons.sh` from the repository root with librsvg, xmllint
and Cargo installed. On macOS the system iconutil also generates the ICNS files.
All PNG, SVG, ICO and ICNS outputs are committed. The
[licence](LICENSE.txt) and [asset index](../../ATTRIBUTION.md) cover the artwork.
