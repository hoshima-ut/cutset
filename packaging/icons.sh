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

render() {
  rsvg-convert --width "$2" --height "$2" --output "$3" "$1"
}

render_channel() {
  local svg="$1" stem="$2" mac="$TMP/$2-mac.svg" size set
  local icons=()
  # Apple's icon grid leaves a transparent margin around the 824/1024 tile.
  sed 's/viewBox="0 0 512 512"/viewBox="-62.14 -62.14 636.27 636.27"/' "$svg" >"$mac"
  grep -q 'viewBox="-62.14' "$mac" || { echo "Unexpected master icon viewBox" >&2; exit 1; }
  render "$mac" 512 "$DIR/$stem-macos-512.png"
  for size in 16 20 24 32 40 48 64 128 256; do
    render "$svg" "$size" "$TMP/$stem-$size.png"
    icons+=("$TMP/$stem-$size.png")
  done
  (cd "$ROOT" && cargo run --quiet --locked -p xtask -- ico "$DIR/$stem.ico" "${icons[@]}")
  if command -v iconutil >/dev/null; then
    set="$TMP/$stem.iconset"
    mkdir -p "$set"
    for size in 16 32 128 256 512; do
      render "$mac" "$size" "$set/icon_${size}x${size}.png"
      render "$mac" $((size * 2)) "$set/icon_${size}x${size}@2x.png"
    done
    iconutil -c icns -o "$DIR/$stem.icns" "$set"
  else
    echo "To regenerate $stem.icns, run packaging/icons.sh on macOS." >&2
  fi
}

cp "$SVG" "$DIR/filmcraft-small.svg"
render "$SVG" 1024 "$DIR/filmcraft-1024.png"
render_channel "$SVG" filmcraft

for size in 16 24 32 48 64 128 256 512; do
  render "$SVG" "$size" "$DIR/hicolor/${size}x${size}/apps/$APP_ID.png"
done
cp "$SVG" "$DIR/hicolor/scalable/apps/$APP_ID.svg"
render "$SVG" 128 "$ROOT/apps/filmcraft-web/web/favicon.png"

# A cooler cut distinguishes the development channel at Dock size.
sed 's/#B8F44A/#8CCDE3/' "$SVG" > "$TMP/nightly.svg"
render_channel "$TMP/nightly.svg" filmcraft-nightly
render "$TMP/nightly.svg" 256 "$DIR/filmcraft-nightly.png"
render "$TMP/filmcraft-nightly-mac.svg" 1024 "$DIR/filmcraft-nightly-1024.png"
