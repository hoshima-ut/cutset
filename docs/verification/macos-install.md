# macOSの配布物を試す

AppleシリコンのMacで、Cargoの既定機能を使ったGUIとCLIを同じソースからビルドし、DMGとCLIのZIPに梱包する手順です。このページでは試用ビルド、正式配布時の受入、旧版の検証記録を扱います。[通常のビルド・署名・公証](../development/build-installer.md)

## ビルドと梱包

Xcode Command Line Tools、Rust 1.95以上を用意し、新しいcloneのルートで実行します。ここでは同じホストでの試用のため、アドホック署名を使います。コード変更後は先に両方のバイナリを再ビルドしてください。

```sh
rustup target add aarch64-apple-darwin
export CARGO_TARGET_DIR="$PWD/target"
export MACOSX_DEPLOYMENT_TARGET=11.0
export FILMCRAFT_BUILD_SHA="$(git rev-parse HEAD)"
cargo build --release --locked --target aarch64-apple-darwin -p filmcraft -p filmcraft-cli
bash packaging/macos/package.sh --arch aarch64 --skip-build --local
```

`--skip-build` は直前に作ったターゲット別のGUIとCLIを使います。通常の出力先は `dist/release` です。`-local.dmg` はデスクトップアプリ、`-local.zip` はCLI、`-local.sha256` は両ファイルの照合値です。

## ビルドしたMacでの確認

1. DMGに `hdiutil verify ファイル名.dmg` を実行し、チェックサムが有効であることを確認します。
2. DMGを開き、空の試用フォルダーに `Cutset.app` をコピーしてDMGを取り出します。コピー先のアプリに `codesign --verify --strict --deep アプリのパス` を実行します。
3. コピー先の実行ファイルに `--demo --data-dir 専用フォルダー` を指定して起動します。編集画面から書き出し画面に移動し、形式と出力先を選べることを確認して編集画面に戻ります。
4. デモのシーケンスにマーカーを一つ追加し、取り消し・やり直しを試します。別名で検証用の案件を保存し、アプリを終了します。
5. CLIのZIPを空のフォルダーに展開します。次の `cutset-cli` を展開した実行ファイルのパスに置き換え、保存した案件を指定して実行します。最後のコマンドにはffprobeを使用します。

```sh
cutset-cli --project manual-smoke.fcproj inspect sequence
cutset-cli --project manual-smoke.fcproj export manual-smoke.mp4 \
  --format h264 --start 0 --end 0.5 --scale 0.25 --gpu-rendering off
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,sample_rate,channels:format=duration \
  -of json manual-smoke.mp4
```

画面だけで書き出す場合は[音量・字幕・MP4の操作手順](../manual/audio-captions-export.md)を参照してください。

## Cutset試用版の実測結果

2026-11-26、AppleシリコンのMacで `0210ec7b` の試用DMGを読み取り専用で開き、空のフォルダーへコピーした `Cutset.app` を起動しました。バージョンは0.20.1、Cargo既定機能でのビルドです。

| 確認項目 | 結果 |
| --- | --- |
| DMGとアプリ | SHA-256、ディスクイメージの整合性、アプリとCLIのアドホック署名を検証。ボリューム名はCutset。Applicationsへのリンクを確認し、Finderレイアウト、背景、アプリアイコンを梱包元と照合。 |
| 識別子 | `io.github.hoshima-ut.cutset`、既存の `.fcproj` の登録は代替エディター（Alternate）。 |
| 編集操作 | コピーしたアプリで編集画面と書き出し画面を切り替え、マーカーの個数が追加・Undo・Redoで4→5→4→5と変わることを確認。保存・終了後、ZIPから展開したCLIで同じ案件を再読込。 |
| 出力と自動化 | MP4の映像はH.264 480×270、音声はAAC 48 kHzステレオ、長さ0.512秒。OMFにもCutsetの作成者情報を確認。CLIの719命令を仕様台帳と照合。 |

このDMGのSHA-256は `6c4513745ce8583c8990c2872df6ee1b146763714059be1423ee4ceca3b28b29`。ダウンロードした際の初回警告や会社管理端末での許可は別端末で確認します。[試用版の開き方](../manual/install.md) ・ [正式版の公開Issue](https://github.com/hoshima-ut/cutset/issues/1)

## 社内配布版を別のMacで受け入れる

署名用Mac以外のMacで、社内の通常の配布経路から正式DMGを取得します。受け渡しと初回起動を、配布先と同じユーザー権限で試します。

1. DMGのSHA-256を配布元の値と照合します。DMGへ `xcrun stapler validate` と `spctl --assess --type open --context context:primary-signature --verbose=2` を実行します。
2. FinderでDMGを開き、Cutsetの背景・アイコン・アプリ名が表示されることを確認します。アプリケーションにコピーし、DMGを取り出します。
3. `codesign -dv --verbose=4 /Applications/Cutset.app` の識別子 `io.github.hoshima-ut.cutset` とTeam IDを照合します。コマンド `xcrun stapler validate /Applications/Cutset.app` と `spctl --assess --type execute --verbose=2 /Applications/Cutset.app` を確認してからFinderで起動します。
4. FilmCraftが入ったMacで、既存の案件のコピーを用意します。Finderの「このアプリケーションで開く」からCutsetを指定し、別名保存・再生・短い書き出しを試します。FilmCraftも従来の場所から起動し、元の案件と設定が開けること、既存の既定アプリの選択が維持されていることを確認します。
5. 前のCutset配布版がある場合は新しい版で置き換え、案件と設定が開くことを確認します。OS・CPU、バージョン、コミット、Team ID、SHA-256、初回起動と共存の結果を記録します。

## 旧FilmCraft名の試用版で確認した結果（履歴）

2026-11-26、Appleシリコン搭載のMac（macOS 27.2.1、Rust 1.99.1）で検証しました。アプリのソースは `1527b422`、APFSで梱包するスクリプトは `3c7a6609`、表示バージョンは `0.20.1` です。この実行ではホストのarm64向けにCargoの既定機能でGUIとCLIをビルドし、専用のターゲット別ディレクトリに2ファイルを置いて `--skip-build` を使いました。追加の音声合成モデルは使用していません。

| 段階 | 実測結果 |
| --- | --- |
| インストール | DMGを読み取り専用で開き、試用フォルダーにアプリをコピーしてディスクを取り出しました。DMGのチェックサム、コピー後のアプリと展開したCLIの署名検査が通りました。 |
| GUI | コピー先のアプリをデモ案件と専用プロファイルで起動しました。［書き出し］と［編集］をクリックして画面の切り替えを確認しました。 |
| 編集・再開 | GUIのコマンド経由でマーカーを追加し、個数が4→5→4→5と変わりました。Undo・Redo後のシーケンス全体が対応する状態と一致し、別名保存・アプリ終了後にCLIで同じマーカーを読み出せました。 |
| 出力 | 配布用ZIPのCLIで0.5秒を指定して書き出しました。ffprobeでH.264映像480×270、AAC音声48 kHzステレオ、MP4の長さ0.512秒を確認しました。 |

この試用DMGのSHA-256は `6e005996d3515300c6c8bd752e85f68680a6baa9070038e497015516b5d453f6` です。別にビルドしたファイルを配る際は、その成果物からSHA-256を取得します。

この表と照合値は旧名称のアドホック署名DMGの記録です。Cutsetの新しい配布物では、ビルドごとの照合値と受入結果を使います。

## 操作マニュアルの編集例を再現する

練習素材が必要な場合は、空の作業フォルダーで次を実行すると、440 Hzの音と映像が入った2秒のMP4を作れます。ffmpegはlibx264とAACエンコーダーが有効なものを使います。

```sh
ffmpeg -f lavfi -i testsrc2=size=320x180:rate=24 \
  -f lavfi -i sine=frequency=440:sample_rate=48000 \
  -t 2 -c:v libx264 -pix_fmt yuv420p -c:a aac -ar 48000 -ac 2 input.mp4
```

2026-11-26に、この素材を空の案件に読み込み、マニュアルと共通の編集エンジンをCLI経由で操作しました。

| 操作 | 確認した結果 |
| --- | --- |
| 素材の6フレーム目（0始まり）から41フレーム目までを挿入し、リンクした映像・音声の末尾を6フレーム短くする | 挿入直後36フレーム、トリム後30、Undo後36、Redo後30。 |
| 音声を−3 dBにし、12フレーム位置で分割して保存する | 開き直した案件で映像・音声ともに12＋18フレーム。入力と出力の定常音を復号して比較した実測値は−3.01 dB。 |
| 日本語字幕「字幕の確認」を入れ、MP4とSRTを書き出す | H.264映像320×180、24 fpsで30フレーム（1.25秒）。音声はAAC、48 kHz、ステレオ。SRTの本文と表示区間（0.250～0.750秒）が一致。 |

画面で操作する手順は[編集](../manual/timeline-editing.md)と[音声・字幕・書き出し](../manual/audio-captions-export.md)にあります。字幕の焼き込みの見た目、音の聴こえ方、OSの保存ダイアログでの操作は個別に確認します。
