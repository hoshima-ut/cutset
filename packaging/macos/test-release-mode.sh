#!/usr/bin/env bash
# Exercise the stable release preflight without a real certificate, network or app build.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
trial="$(mktemp -d)"
trap 'rm -rf "$trial"' EXIT
mkdir "$trial/bin"
cat > "$trial/bin/security" <<'MOCK'
#!/bin/sh
printf 'security\n' >> "$TRACE"
printf '  1) %040d "Developer ID Application: Test Signer (TESTTEAM01)"\n' 1
MOCK
cat > "$trial/bin/xcrun" <<'MOCK'
#!/bin/sh
[ "$1 $2" = "notarytool history" ] || exit 4
printf 'notary %s\n' "$3" >> "$TRACE"
[ -z "${REJECT_AUTH:-}" ]
MOCK
cat > "$trial/bin/cargo" <<'MOCK'
#!/bin/sh
for key in APPLE_CERTIFICATE APPLE_CERTIFICATE_PASSWORD KEYCHAIN_PASSWORD APPLE_ID APPLE_PASSWORD APPLE_TEAM_ID; do
  if printenv "$key" >/dev/null; then exit 12; fi
done
printf 'cargo\n' >> "$TRACE"
# Stop where compilation would begin (including for --local).
exit 42
MOCK
chmod +x "$trial/bin/"*
identity='Developer ID Application: Test Signer (TESTTEAM01)'
fingerprint="$(printf '%040d' 1)"
probe() {
  local expected="$1" trace="$2" code=0
  shift 2
  : > "$trial/trace"
  env -i PATH="$trial/bin:/usr/bin:/bin:/usr/sbin:/sbin" TRACE="$trial/trace" DIST="$trial/dist" \
    "$@" > "$trial/log" 2>&1 || code=$?
  if [[ "$code" != "$expected" || "$(cat "$trial/trace")" != "$trace" ]]; then
    echo "unexpected exit $code or preflight trace:" >&2
    cat "$trial/trace" "$trial/log" >&2
    exit 1
  fi
  [[ -z "$(ls -A "$trial/dist" 2>/dev/null)" ]] || { echo "failed package was published" >&2; exit 1; }
}

script="$here/package.sh"
probe 1 '' bash "$script"
probe 1 '' MACOS_SIGN_IDENTITY=- CUTSET_NOTARY_PROFILE=trial bash "$script"
probe 1 '' MACOS_SIGN_IDENTITY="$identity" bash "$script"
probe 1 'security' MACOS_SIGN_IDENTITY=unavailable CUTSET_NOTARY_PROFILE=trial bash "$script"
probe 1 $'security\nnotary --keychain-profile' MACOS_SIGN_IDENTITY="$identity" CUTSET_NOTARY_PROFILE=trial REJECT_AUTH=1 bash "$script"
probe 42 $'security\nnotary --keychain-profile\ncargo' MACOS_SIGN_IDENTITY="$fingerprint" CUTSET_NOTARY_PROFILE=trial bash "$script"
probe 1 '' MACOS_SIGN_IDENTITY="$identity" APPLE_ID=fixture APPLE_PASSWORD=fixture APPLE_TEAM_ID=TESTTEAM01 bash "$script"
probe 42 $'security\nnotary --keychain-profile\ncargo' MACOS_SIGN_IDENTITY="$identity" CUTSET_NOTARY_PROFILE=trial APPLE_ID=fixture \
  APPLE_PASSWORD=fixture APPLE_TEAM_ID=TESTTEAM01 APPLE_CERTIFICATE=fixture APPLE_CERTIFICATE_PASSWORD=fixture KEYCHAIN_PASSWORD=fixture bash "$script"
probe 42 'cargo' MACOS_SIGN_IDENTITY="$identity" CUTSET_NOTARY_PROFILE=trial bash "$script" --local
# A misfiled binary must never be labelled with the requested architecture, including --skip-build.
cat > "$trial/bin/lipo" <<'MOCK'
#!/bin/sh
if [ "$1" = "-archs" ]; then
  printf 'slices %s\n' "${2##*/}" >> "$TRACE"
  case "${2##*/}" in
    filmcraft) echo "$GUI_SLICES" ;;
    filmcraft-cli) echo "$CLI_SLICES" ;;
  esac
fi
MOCK
chmod +x "$trial/bin/lipo"
probe 1 'slices filmcraft' GUI_SLICES=x86_64 CLI_SLICES=arm64 bash "$script" --local --arch aarch64 --skip-build
probe 1 $'slices filmcraft\nslices filmcraft-cli' GUI_SLICES='x86_64 arm64' CLI_SLICES=arm64 bash "$script" --local --arch universal --skip-build
echo "macOS release preflight: 11 cases passed"
