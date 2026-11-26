# Cutset installer window

Finder displays the application and an Applications folder link on a 660 × 400 pt
background. The editable [vector](background.svg) contains the Cutset wordmark,
two timeline tracks, a direction arrow, and an installation instruction. The
Inter wordmark and instruction are outlines so rendering does not depend on the
host's fonts. The light background keeps Finder's icon labels legible.

The layout places `Cutset.app` at (170, 212) and `Applications` at (490, 212).
The volume name `Cutset` must match the background alias in the DS_Store and the
name used by [package.sh](../package.sh). The alias resolves
`/.background/background.tiff` on that volume.

To regenerate, install librsvg (`rsvg-convert`) and run the following in a
Python virtual environment from the repository root.

```sh
python -m pip install 'pillow>=12' ds_store==1.3.3 mac_alias==2.2.3
python packaging/macos/dmg/generate.py
```

The committed TIFF contains 660 × 400 and 1320 × 800 pages at 72 and 144 dpi.
The DS_Store uses fixed metadata and carries no local user paths. The generated
files are copied into the DMG during packaging.
