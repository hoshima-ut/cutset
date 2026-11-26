# ソースからインストーラーを作る

ここでは手元のソースからOS別の配布物を作ります。デスクトップの動作を試すだけなら、まず以下の「準備」でGUIを直接起動できます。ビルドと検証はローカルで行います。GitHub Actionsは停止中です。

## 準備

新しく取得する場合は次を実行します。すでにcloneしている場合は、そのリポジトリ直下から始めてください。

```sh
git clone https://github.com/hoshima-ut/cutset.git
cd cutset
git rev-parse --short HEAD
rustc --version
cargo --version
```

Rustの最低バージョンは1.95です。各OSのコンパイラーと開発用ライブラリも先に用意します。既定の成果物の保存先は `dist/release/`、中間ファイルの保存先は `target/` です。別の場所を使う場合は、それぞれ `DIST` と `CARGO_TARGET_DIR` に専用ディレクトリの絶対パスを指定します。取得するRust依存関係は `Cargo.lock` で固定しています。ネットワークのない環境では、対象のRustツールチェーン、ターゲット、OS別のツールを事前に用意し、つながる環境で同じコミットの `cargo fetch --locked` を実行してCargoキャッシュを準備します。準備後にCargoの通信を止める場合、bashではビルドコマンドの先頭に `CARGO_NET_OFFLINE=true` を付けます。PowerShellでは先に `$env:CARGO_NET_OFFLINE = "true"` を実行します。[Rustの開発環境](rust.md) ・ [ワークスペース設定](../../Cargo.toml)

環境を用意したら、まず端末でバージョンを確認します。2行目は空の案件で編集画面を起動し、試用中の設定や復旧データを専用フォルダーに分けます。

```sh
cargo run --locked --release -p filmcraft-cli -- --version
cargo run --locked --release -p filmcraft -- --empty --data-dir ./target/cutset-trial-profile
```

## macOSの配布用DMGとCLIを作る

組織の署名を扱うMacに、秘密鍵付きの「Developer ID Application」証明書と、`notarytool` および `stapler` が使えるXcodeのツールを用意します。配布対象はAppleシリコンなら `aarch64`、Intelなら `x86_64`、両方なら `universal` です。以下は両方のCPUに対応する例です。証明書の発行やAppleへの組織登録から始める場合は、[初回の署名設定](macos-signing.md)を確認してください。

```sh
rustup target add aarch64-apple-darwin x86_64-apple-darwin
security find-identity -v -p codesigning
xcrun notarytool store-credentials "cutset-notary"
```

最後のコマンドは初回だけ実行します。組織のApple ID・Team ID・アプリ用パスワード等は対話入力し、キーチェーンに保存します。ビルド時に使うのはプロファイル名と、前の一覧にある署名証明書のSHA-1指紋または完全な表示名です。次の例の「証明書のSHA-1指紋」を自組織の値に置き換えます。[Appleの公証手順](https://developer.apple.com/documentation/security/customizing-the-notarization-workflow)

```sh
export MACOS_SIGN_IDENTITY='証明書のSHA-1指紋'
export CUTSET_NOTARY_PROFILE='cutset-notary'
bash packaging/macos/package.sh --arch universal
```

スクリプトは証明書とAppleへの認証を先に検査し、GUIとCLIをビルドします。アプリとDMGを署名・公証してチケットを添付し、Gatekeeperの評価も確認します。CLIのZIPも公証します。単体のCLIにはチケットを添付できないため、macOSは必要に応じてオンラインで確認します。標準ビルドには追加の音声合成機能も含まれます。[パッケージ処理](../../packaging/macos/package.sh)

`dist/release/` に同じ版・CPUの3ファイルが揃います。以下はバージョン0.20.1での照合例です。別の版は実際のファイル名に置き換えます。

```sh
cd dist/release
shasum -a 256 -c cutset-0.20.1-macos-universal.sha256
xcrun stapler validate cutset-0.20.1-macos-universal.dmg
spctl --assess --type open --context context:primary-signature --verbose=2 cutset-0.20.1-macos-universal.dmg
```

`.dmg` は編集者用、`cutset-cli-…zip` は自動化用です。配布担当は、作成元コミット、版、CPU、署名者・Team ID、公証結果、SHA-256を記録します。利用者には社内の配布経路から対象のDMGと照合値を案内します。別のMacでの初回起動、FilmCraftとの共存、案件の開閉は[導入検証](../verification/macos-install.md)に沿って確認します。

## 自分のMacで試す

自分のMac上で動作を確認する場合は `--local` を指定します。アドホック署名は署名後に中身が変更されたかを検査できます。開発元を証明する署名とAppleの公証は正式配布時に加えます。

```sh
rustup target add aarch64-apple-darwin
bash packaging/macos/package.sh --arch aarch64 --local
```

ビルドしたMacで `dist/release/cutset-バージョン-macos-aarch64-local.dmg` を開き、空の試用フォルダーへ `Cutset.app` をコピーします。IntelのMacではターゲットと `--arch` を `x86_64` 用に変更します。Cargoの既定機能で試す場合は[最小構成の検証手順](../verification/macos-install.md)を使います。

## macOS以外の配布状況

以下は上流の生成手順を開発・検証するための資料です。Windows・Linux・FreeBSDのCutset社内配布は、既存版とのインストール先・製品識別子の分離と、各OSでの受入確認が残っています。

## WindowsでMSIとポータブル版を作る

WindowsでPowerShell 7、MSVCのC++ビルドツール、Windows SDK、.NET SDK、WiX 5.0.2を使います。x64の例です。WiX本体、拡張、Rustターゲットの導入にはパッケージの取得が必要です。スクリプトもビルド時にWiXのUI拡張の追加を呼び出します。[パッケージスクリプト](../../packaging/windows/package.ps1)

```powershell
rustup target add x86_64-pc-windows-msvc
dotnet tool install --global wix --version 5.0.2
wix extension add -g WixToolset.UI.wixext/5.0.2
pwsh ./packaging/windows/package.ps1 -Arch x64
Get-ChildItem ./dist/release
```

出力は `filmcraft-<version>-windows-x64.msi` と `…-portable.zip` です。既存のFilmCraftと同じPCで試す場合は、ZIPを別のフォルダーに展開して `filmcraft.exe` を起動します。`portable.txt` を同じ場所に残すと設定などを隣の `cutset-data/` に置きます。MSIは既存製品とUpgradeCodeを共有し、同じ版でも置換できます。インストーラー検証には独立したWindows環境を使用します。既定は現在のユーザーへのインストールで、全ユーザーも選べます。[インストール仕様](../../packaging/windows/INSTALLATION.md) ・ [MSI定義](../../packaging/windows/filmcraft.wxs)

32ビット版は `-Arch x86` と `i686-pc-windows-msvc`、ARM64版は `-Arch arm64` と `aarch64-pc-windows-msvc` を使います。ARM64には対応するMSVCツールも必要です。署名情報がない場合もローカル試用のMSIとZIPを作成できます。社内配布でAuthenticode署名を使う場合はEXEとMSIの署名者を確認します。[署名設定](../../packaging/windows/sign.ps1)

## Linuxでtar、deb、rpmを作る

ビルドするLinux環境にC/C++のツールチェーン、ALSA、GTK 3、X11・Waylandの開発用ライブラリを用意します。まずtarを作る例です。展開先の `bin/filmcraft-cli --version` でCLIを、`bin/filmcraft --empty --data-dir <専用フォルダー>` でGUIを確認できます。[開発環境](rust.md) ・ [Linuxパッケージ](../../packaging/linux/package.sh)

```sh
bash packaging/linux/package.sh --formats tar
ls -lh dist/release
```

`nfpm` を用意して `--formats "deb rpm tar"` とすると、同じビルドからパッケージを3種類作れます。deb・rpmは上流と同じパッケージ名 `filmcraft` を登録します。既存環境での試用には、独立した場所に展開できるtarが適しています。

AppImageは同じスクリプトの `--formats appimage`、Flatpakは同じCPU向けのtarを用意して `bash packaging/linux/flatpak-bundle.sh` を使います。AppImageはツールやランタイムが未取得ならダウンロードします。Flatpak用のスクリプトはFlathubからSDK等を導入し、既定で作成したバンドルを現在のユーザーにインストールして検証します。オフラインでの最初の試用にはtarを使えます。[AppImageの作成処理](../../packaging/linux/package.sh) ・ [Flatpakの作成とインストール](../../packaging/linux/flatpak-bundle.sh)

## FreeBSDでtarを作る

FreeBSDホスト上でbash、Rust、コンパイラー、GTK 3、fontconfig、alsa-lib、ウィンドウ・描画用の開発ライブラリを用意します。上流のビルド資料はFreeBSD 14.3を対象としています。スクリプトはx86_64とaarch64の名前に対応します。出力にはGUIとCLI、デスクトップ登録用ファイル、ライセンスが入ります。[上流のFreeBSDビルド情報](../reference/filmcraft/releasing.md) ・ [FreeBSDパッケージ](../../packaging/freebsd/package.sh)

```sh
bash packaging/freebsd/package.sh
tar -tzf dist/release/filmcraft-*-freebsd-*.tar.gz | head
```

生成物を専用フォルダーへ展開して `bin/filmcraft-cli --version` を確認します。`--dry-run` はスタブを使って梱包レイアウトを確認するオプションです。

## 配布前に確認すること

- **版と成果物**。作成元コミット、対象OS・CPU、アプリの表示バージョン、成果物のSHA-256を記録します。macOSは `shasum -a 256 <DMG>`、Windowsは `Get-FileHash <MSI> -Algorithm SHA256`、Linuxは `sha256sum <パッケージ>`、FreeBSDは `sha256 <tarball>` で照合できます。
- **既存版との共存**。社内に独立したCutsetとして導入する前に、アプリの表示名、インストール先、OSの製品ID・ファイル関連付け、設定・復旧先を確認します。FilmCraft入りの検証環境でインストール、既存案件の再開、更新、アンインストールを試し、両方のデータを確認します。[上流パッケージの扱い](../reference/filmcraft/releasing.md)
- **更新先と署名者**。アプリ内更新先の設定は `hoshima-ut/cutset` です。LinuxのAppImageは作成時の `GITHUB_REPOSITORY` で参照先を変更できます。配布時の設定と署名者を記録し、認証情報はOSの秘密情報ストアや管理された署名環境から渡します。[アプリの更新先](../../crates/ui-egui/src/lib.rs) ・ [Linuxの更新設定](../../packaging/linux/package.sh) ・ [認証情報の扱い](../security/credentials.md)
