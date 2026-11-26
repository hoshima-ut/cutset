#!/usr/bin/env bash
# Build a Cutset DMG and CLI ZIP. Default: signed and notarized for distribution.
#
# Usage: packaging/macos/package.sh [--arch universal|aarch64|x86_64] [--skip-build] [--local]
#
# Distribution: set MACOS_SIGN_IDENTITY to the full Developer ID Application name or fingerprint,
# and CUTSET_NOTARY_PROFILE to a notarytool Keychain profile. MACOS_KEYCHAIN optionally selects
# the signing keychain. This command submits archives to Apple for notarization.
# --local: ad-hoc sign for the build Mac. Never contact the notary service. Names end in -local.
# --skip-build: package binaries from CARGO_TARGET_DIR/<target>/release.
set -euo pipefail
set +x

ARCH=universal
SKIP_BUILD=0
LOCAL=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --arch) [[ $# -gt 1 ]] || { echo "missing value for --arch" >&2; exit 2; }; ARCH="$2"; shift 2 ;;
    --skip-build) SKIP_BUILD=1; shift ;;
    --local) LOCAL=1; shift ;;
    -h | --help) sed -n '2,10p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done
case "$ARCH" in
  universal) TARGETS=(aarch64-apple-darwin x86_64-apple-darwin) ;;
  aarch64) TARGETS=(aarch64-apple-darwin) ;;
  x86_64) TARGETS=(x86_64-apple-darwin) ;;
  *) echo "unknown --arch $ARCH" >&2; exit 2 ;;
esac

fail() { echo "error: $*" >&2; exit 1; }
SIGN_KEYCHAIN=()
SUFFIX=""
if [[ "$LOCAL" = 1 ]]; then
  IDENTITY="-"
  SUFFIX="-local"
else
  IDENTITY="${MACOS_SIGN_IDENTITY:-}"
  [[ -n "$IDENTITY" && "$IDENTITY" != "-" ]] || fail "distribution requires MACOS_SIGN_IDENTITY (Developer ID Application); --local builds an ad-hoc trial"
  [[ -n "${CUTSET_NOTARY_PROFILE:-}" ]] || fail "distribution requires CUTSET_NOTARY_PROFILE (notarytool Keychain profile)"
  if [[ -n "${MACOS_KEYCHAIN:-}" ]]; then SIGN_KEYCHAIN=(--keychain "$MACOS_KEYCHAIN"); fi
fi
# Build scripts and unrelated subprocesses need none of the legacy signing secrets.
unset APPLE_ID APPLE_PASSWORD APPLE_TEAM_ID APPLE_CERTIFICATE APPLE_CERTIFICATE_PASSWORD KEYCHAIN_PASSWORD
if [[ "$LOCAL" = 0 ]]; then
  identities="$(security find-identity -v -p codesigning ${MACOS_KEYCHAIN:+"$MACOS_KEYCHAIN"})"
  # Resolve the exact requested Developer ID Application name or SHA-1 before building.
  IDENTITY="$(printf '%s\n' "$identities" | awk -F '"' -v wanted="$IDENTITY" '
    $2 ~ /^Developer ID Application: / {
      n=split($1, fields, /[[:space:]]+/)
      sha=fields[n-1]
      if ($2 == wanted || (length(wanted)==40 && toupper(sha)==toupper(wanted))) { print sha; count++ }
    }
    END { if (count != 1) exit 1 }')" || fail "expected one valid matching Developer ID Application signing identity"
  # This read-only query confirms the notary credentials before any archive is built or submitted.
  xcrun notarytool history --keychain-profile "$CUTSET_NOTARY_PROFILE" >/dev/null || fail "unable to authenticate to Apple's notary service"
fi

# shellcheck source=../env.sh
. "$(dirname "${BASH_SOURCE[0]}")/../env.sh"
HERE="$ROOT/packaging/macos"
# Keep in sync with LSMinimumSystemVersion in Info.plist.in.
export MACOSX_DEPLOYMENT_TARGET=11.0
[[ "$VERSION" =~ ^([0-9]+\.[0-9]+\.[0-9]+)([-+][A-Za-z0-9.+-]+)?$ ]] || fail "invalid package version"
SHORT_VERSION="${BASH_REMATCH[1]}"
[[ -z "${FILMCRAFT_BUILD_SHA:-}" || "$FILMCRAFT_BUILD_SHA" =~ ^[0-9a-f]{40}$ ]] || fail "invalid source commit for CutsetBuildCommit"
echo "==> Cutset $VERSION for macOS ($ARCH), local: $LOCAL"

# ---- build -------------------------------------------------------------------------------------
if [[ "$SKIP_BUILD" = 0 ]]; then
  args=()
  for t in "${TARGETS[@]}"; do args+=(--target "$t"); done
  # Official packages include Kokoro natural voices (downloaded on first use). #2318 #3773
  (cd "$ROOT" && cargo build --release --locked -p filmcraft -p filmcraft-cli --features filmcraft/neural-voices "${args[@]}")
fi

# Stage both artifacts privately. Failed verification leaves previous releases intact.
WORK="$(mktemp -d "$DIST/.cutset-package.XXXXXXXX")"
trap 'rm -rf "$WORK"' EXIT
APP="$WORK/Cutset.app"
DMG="$WORK/cutset-$VERSION-macos-$ARCH$SUFFIX.dmg"
CLI_ZIP="$WORK/cutset-cli-$VERSION-macos-$ARCH$SUFFIX.zip"
mkdir "$WORK/bin"
for bin in filmcraft filmcraft-cli; do
  inputs=()
  for t in "${TARGETS[@]}"; do inputs+=("$CARGO_TARGET_DIR/$t/release/$bin"); done
  lipo -create -output "$WORK/bin/$bin" "${inputs[@]}"
  slices="$(lipo -archs "$WORK/bin/$bin")"
  case "$ARCH:$slices" in
    aarch64:arm64 | x86_64:x86_64 | "universal:arm64 x86_64" | "universal:x86_64 arm64") ;;
    *) fail "$bin contains '$slices', expected '$ARCH'" ;;
  esac
done

# ---- signing helpers ---------------------------------------------------------------------------
sign() {
  # Hardened runtime + secure timestamp for a real identity; ad-hoc can't be timestamped.
  local ts=(--timestamp)
  [[ "$IDENTITY" = "-" ]] && ts=(--timestamp=none)
  codesign --force --sign "$IDENTITY" ${SIGN_KEYCHAIN[@]+"${SIGN_KEYCHAIN[@]}"} "${ts[@]}" "$@"
}

# `stapler staple` and `stapler validate` both fetch the ticket from Apple's CloudKit, and a dropped
# connection there (NSURLErrorDomain -1005, "Error 68") fails them although notarization worked.
# Both are idempotent, so retry with a pause; a missing or bad ticket still fails every try.
stapler_retry() {
  local try
  for try in 1 2 3 4; do
    xcrun stapler "$1" "$2" && return 0
    [[ "$try" = 4 ]] && break
    echo "stapler $1 failed (try $try of 4); retrying in $((try * 20)) s" >&2
    sleep $((try * 20))
  done
  echo "error: stapler $1 $(basename "$2") failed 4 times" >&2
  exit 1
}

notarize() {
  local file="$1" out id status code=0
  echo "==> notarizing $(basename "$file") (this can take a few minutes)"
  out="$(xcrun notarytool submit "$file" --keychain-profile "$CUTSET_NOTARY_PROFILE" --wait --timeout 1h --output-format json)" || code=$?
  echo "$out"
  id="$(printf '%s' "$out" | plutil -extract id raw -o - - 2>/dev/null || true)"
  status="$(printf '%s' "$out" | plutil -extract status raw -o - - 2>/dev/null || true)"
  if [[ "$code" != 0 || "$status" != "Accepted" ]]; then
    if [[ -n "$id" ]]; then
      xcrun notarytool log "$id" --keychain-profile "$CUTSET_NOTARY_PROFILE" || true
    fi
    echo "error: notarization of $(basename "$file") failed (status: ${status:-unknown})" >&2
    exit 1
  fi
}

# The source NOTICE points to these paths for the fonts embedded in every build.
copy_asset_notices() {
  local resources="$1"
  cp "$ROOT/ATTRIBUTION.md" "$resources/"
  mkdir -p "$resources/assets/fonts"
  cp "$ROOT"/assets/fonts/OFL-*.txt "$resources/assets/fonts/"
}

# ---- Cutset.app ----------------------------------------------------------------------------
echo "==> assembling $APP"
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources"
# Executable and icon carry the display name (CFBundleExecutable / CFBundleIconFile).
cp "$WORK/bin/filmcraft" "$APP/Contents/MacOS/Cutset"
cp "$ROOT/assets/app-icon/filmcraft.icns" "$APP/Contents/Resources/Cutset.icns"
cp "$ROOT/NOTICE" "$ROOT/LICENSE-MIT" "$ROOT/LICENSE-APACHE" "$APP/Contents/Resources/"
copy_asset_notices "$APP/Contents/Resources"
sed -e "s/@VERSION@/$VERSION/g" -e "s/@SHORT_VERSION@/$SHORT_VERSION/g" \
  -e "s/@BUILD_SHA@/${FILMCRAFT_BUILD_SHA:-unknown}/g" \
  "$HERE/Info.plist.in" >"$APP/Contents/Info.plist"
plutil -lint "$APP/Contents/Info.plist"
printf 'APPL????' >"$APP/Contents/PkgInfo"
# licences of the embedded craft-fonts fonts (builds with CRAFT_FONTS_DIR)
copy_font_licences "$APP/Contents/Resources"

# Sign inside-out: nested code first, then the bundle itself (no --deep on the final signature).
# Today the only nested code is the main executable; frameworks/helpers would be signed here too.
sign --options runtime --entitlements "$HERE/entitlements.plist" "$APP/Contents/MacOS/Cutset"
sign --options runtime --entitlements "$HERE/entitlements.plist" "$APP"
codesign --verify --strict --deep --verbose=2 "$APP"

if [[ "$LOCAL" = 0 ]]; then
  codesign --verify --strict -R='anchor apple generic and certificate leaf[field.1.2.840.113635.100.6.1.13] exists' "$APP"
  ditto -c -k --keepParent "$APP" "$WORK/Cutset-notarize.zip"
  notarize "$WORK/Cutset-notarize.zip"
  stapler_retry staple "$APP"
  stapler_retry validate "$APP"
  spctl --assess --type execute -vvv "$APP"
fi

# ---- DMG ---------------------------------------------------------------------------------------
echo "==> building $DMG"
STAGE="$WORK/dmg"
mkdir -p "$STAGE"
ditto "$APP" "$STAGE/Cutset.app"
ln -s /Applications "$STAGE/Applications"
# Finder window layout: background, icon size and positions (packaging/macos/dmg/README.md).
mkdir -p "$STAGE/.background"
cp "$HERE/dmg/background.tiff" "$STAGE/.background/background.tiff"
cp "$HERE/dmg/dmg-layout.DS_Store" "$STAGE/.DS_Store"
# HFS hybrid authoring adds FinderInfo to bundle entries when the app is copied to APFS.
# Preserve the signed bundle's metadata across installation and keep the Finder layout's volume name.
hdiutil create -fs APFS -format UDZO -imagekey zlib-level=9 -volname "Cutset" \
  -srcfolder "$STAGE" "$DMG"
sign "$DMG"
codesign --verify --strict --verbose=2 "$DMG"
if [[ "$LOCAL" = 0 ]]; then
  notarize "$DMG"
  stapler_retry staple "$DMG"
  stapler_retry validate "$DMG"
  spctl --assess --type open --context context:primary-signature -vvv "$DMG"
fi

# ---- CLI ---------------------------------------------------------------------------------------
echo "==> building $CLI_ZIP"
CLI_DIR="$WORK/cutset-cli-$VERSION-macos-$ARCH$SUFFIX"
mkdir "$CLI_DIR"
cp "$WORK/bin/filmcraft-cli" "$CLI_DIR/cutset-cli"
copy_docs "$CLI_DIR"
copy_asset_notices "$CLI_DIR"
sign --options runtime "$CLI_DIR/cutset-cli"
codesign --verify --strict --verbose=2 "$CLI_DIR/cutset-cli"
ditto -c -k --keepParent "$CLI_DIR" "$CLI_ZIP"
# A bare Mach-O cannot carry a stapled ticket; Gatekeeper looks the notarization up online.
if [[ "$LOCAL" = 0 ]]; then notarize "$CLI_ZIP"; fi

case "$ARCH:$(uname -m)" in
  universal:* | aarch64:arm64 | x86_64:x86_64) "$CLI_DIR/cutset-cli" --version ;;
esac
MANIFEST="$WORK/cutset-$VERSION-macos-$ARCH$SUFFIX.sha256"
(cd "$WORK" && shasum -a 256 "$(basename "$DMG")" "$(basename "$CLI_ZIP")") > "$MANIFEST"
mv -f "$DMG" "$CLI_ZIP" "$MANIFEST" "$DIST/"
echo "==> done"
ls -lh "$DIST/$(basename "$DMG")" "$DIST/$(basename "$CLI_ZIP")" "$DIST/$(basename "$MANIFEST")"
