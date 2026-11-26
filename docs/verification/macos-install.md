# macOSの配布物を試す

AppleシリコンのMacで、Cargoの既定機能を使ったGUIとCLIを同じソースからビルドし、DMGとCLIのZIPに梱包する手順です。通常の配布ビルドでは追加の音声合成機能も有効になります。[通常のビルド・署名・公証](../development/build-installer.md)

## ビルドと梱包

Xcode Command Line Tools、Rust 1.95以上を用意し、新しいcloneのルートで実行します。ここでは同じホストでの試用のため、アドホック署名を使います。コード変更後は先に両方のバイナリを再ビルドしてください。

```sh
rustup target add aarch64-apple-darwin
export CARGO_TARGET_DIR="$PWD/target"
export MACOSX_DEPLOYMENT_TARGET=11.0
export FILMCRAFT_BUILD_SHA="$(git rev-parse HEAD)"
cargo build --release --locked --target aarch64-apple-darwin -p filmcraft -p filmcraft-cli
MACOS_SIGN_IDENTITY=- bash packaging/macos/package.sh --arch aarch64 --skip-build
```

`--skip-build` は直前に作ったターゲット別のGUIとCLIを使います。通常の出力先は `dist/release` です。DMGはデスクトップアプリ、ZIPは検査や自動処理に使うCLIです。GUIを使う方にはDMGだけで足ります。

## インストール後の確認

1. DMGに `hdiutil verify ファイル名.dmg` を実行し、チェックサムが有効であることを確認します。
2. DMGを開き、空の試用フォルダーに `FilmCraft.app` をコピーしてDMGを取り出します。コピー先のアプリに `codesign --verify --strict --deep アプリのパス` を実行します。
3. コピー先の実行ファイルに `--demo --data-dir 専用フォルダー` を指定して起動します。編集画面から書き出し画面に移動し、形式と出力先を選べることを確認して編集画面に戻ります。
4. デモのシーケンスにマーカーを一つ追加し、取り消し・やり直しを試します。別名で検証用の案件を保存し、アプリを終了します。
5. CLIのZIPを空のフォルダーに展開します。次の `filmcraft-cli` を展開した実行ファイルのパスに置き換え、保存した案件を指定して実行します。最後のコマンドにはffprobeを使用します。

```sh
filmcraft-cli --project manual-smoke.fcproj inspect sequence
filmcraft-cli --project manual-smoke.fcproj export manual-smoke.mp4 \
  --format h264 --start 0 --end 0.5 --scale 0.25 --gpu-rendering off
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,sample_rate,channels:format=duration \
  -of json manual-smoke.mp4
```

画面だけで書き出す場合は[音量・字幕・MP4の操作手順](../manual/audio-captions-export.md)を参照してください。
