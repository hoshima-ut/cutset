#!/usr/bin/env bash
# Regenerate the committed Cutset icons from the canonical vector. Install librsvg for rsvg-convert.
# macOS iconutil generates the ICNS assets in addition to the platform-independent outputs.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DIR="$ROOT/assets/app-icon"
SVG="$DIR/filmcraft.svg"
APP_ID="ai.storyteller.filmcraft"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

# Both square layouts reuse the exact path IDs of the approved six-letter wordmark.
# Each generated SVG contains its outlines so it is also portable on its own.
compose() {
  local layout="$1" output="$2"
  {
    cat <<'SVG'
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 512 512">
  <title>Cutset</title>
  <rect width="512" height="512" rx="105" fill="#FFFFFF"/>
  <defs>
SVG
    # The master uses one path per letter. XPath keeps this independent of line wrapping.
    xmllint --xpath '/*/*[local-name()="path"]' "$DIR/cutset-wordmark.svg"
    echo '  </defs>'
    if [[ "$layout" == small ]]; then
      cat <<'SVG'
  <use xlink:href="#letter-c" transform="translate(45 130) scale(.685) translate(-80 -263)"/>
  <use xlink:href="#letter-s" transform="translate(276 130) scale(.685) translate(-1022 -263)"/>
SVG
    else
      cat <<'SVG'
  <g transform="translate(57 48) scale(.42) translate(-80 -169)">
    <use xlink:href="#letter-c"/><use xlink:href="#letter-u"/><use xlink:href="#letter-t-one"/>
  </g>
  <g transform="translate(71 265) scale(.42) translate(-1022 -169)">
    <use xlink:href="#letter-s"/><use xlink:href="#letter-e"/><use xlink:href="#letter-t-two"/>
  </g>
SVG
    fi
    echo '</svg>'
  } > "$output"
}

render() {
  local source="$1" logical_size="${5:-$3}"
  if (( logical_size < 32 )); then source="$2"; fi
  rsvg-convert --width "$3" --height "$3" --output "$4" "$source"
}

render_channel() {
  local svg="$1" small="$2" stem="$3" mac="$TMP/$3-mac.svg" mac_small="$TMP/$3-mac-small.svg" size set
  local icons=()
  # Apple's icon grid leaves a transparent margin around the 824/1024 tile.
  sed 's/viewBox="0 0 512 512"/viewBox="-62.14 -62.14 636.27 636.27"/' "$svg" >"$mac"
  sed 's/viewBox="0 0 512 512"/viewBox="-62.14 -62.14 636.27 636.27"/' "$small" >"$mac_small"
  grep -q 'viewBox="-62.14' "$mac" || { echo "Unexpected master icon viewBox" >&2; exit 1; }
  render "$mac" "$mac_small" 512 "$DIR/$stem-macos-512.png"
  for size in 16 20 24 32 40 48 64 128 256; do
    render "$svg" "$small" "$size" "$TMP/$stem-$size.png"
    icons+=("$TMP/$stem-$size.png")
  done
  (cd "$ROOT" && cargo run --quiet --locked -p xtask -- ico "$DIR/$stem.ico" "${icons[@]}")
  if command -v iconutil >/dev/null; then
    set="$TMP/$stem.iconset"
    mkdir -p "$set"
    for size in 16 32 128 256 512; do
      render "$mac" "$mac_small" "$size" "$set/icon_${size}x${size}.png"
      render "$mac" "$mac_small" $((size * 2)) "$set/icon_${size}x${size}@2x.png" "$size"
    done
    iconutil -c icns -o "$DIR/$stem.icns" "$set"
  else
    echo "To regenerate $stem.icns, run packaging/icons.sh on macOS." >&2
  fi
}

small="$DIR/filmcraft-small.svg"
rsvg-convert --width 512 --output "$DIR/cutset-wordmark.png" "$DIR/cutset-wordmark.svg"
compose full "$SVG"
compose small "$small"

render "$SVG" "$small" 1024 "$DIR/filmcraft-1024.png"
render_channel "$SVG" "$small" filmcraft

for size in 16 24 32 48 64 128 256 512; do
  render "$SVG" "$small" "$size" "$DIR/hicolor/${size}x${size}/apps/$APP_ID.png"
done
cp "$SVG" "$DIR/hicolor/scalable/apps/$APP_ID.svg"
# Browsers downsample this PNG to tab size, so export the compact lettering.
render "$small" "$small" 128 "$ROOT/apps/filmcraft-web/web/favicon.png"

# Nightly keeps the approved lettering and uses a lavender tile and a purple baseline.
nightly() {
  sed -e 's/#FFFFFF/#E5D6F3/' \
      -e 's|</svg>|  <rect x="192" y="476" width="128" height="12" rx="6" fill="#673B99"/></svg>|' "$1" > "$2"
}
nightly "$SVG" "$TMP/nightly.svg"
nightly "$small" "$TMP/nightly-small.svg"
render_channel "$TMP/nightly.svg" "$TMP/nightly-small.svg" filmcraft-nightly
render "$TMP/nightly.svg" "$TMP/nightly-small.svg" 256 "$DIR/filmcraft-nightly.png"
render "$TMP/filmcraft-nightly-mac.svg" "$TMP/filmcraft-nightly-mac-small.svg" 1024 "$DIR/filmcraft-nightly-1024.png"
