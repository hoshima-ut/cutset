# Cutset app icon

The Cutline mark shows two offset timeline tracks crossed by a diagonal cut. The stable
palette uses a graphite field (`#18221F`), warm white (`#F6F5EF`) and lime (`#B8F44A`).
The nightly artwork uses `#8CCDE3` at the cut so the channels can be distinguished in the Dock.

The editable master is [filmcraft.svg](filmcraft.svg). Internal asset paths retain the names
used by the Rust crates and native packagers. The SVG viewBox is 512 × 512. macOS images
center the tile within an 824/1024 safe area. Windows, Linux and the web use the full tile.

Run `bash packaging/icons.sh` from the repository root with librsvg and Cargo installed.
Run it on macOS to regenerate the ICNS files using the system iconutil. The PNGs, scalable
SVG, ICOs, ICNS files, and browser favicon are committed so applications build directly
from a clone. Each asset has a provenance sidecar. The [licence](LICENSE.txt) and
[asset index](../../ATTRIBUTION.md) apply to the new Cutset artwork.
