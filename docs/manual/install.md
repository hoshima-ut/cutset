# インストールと初回起動

社内の配布担当から、自分のOS・CPUに合うファイル、対象バージョン、SHA-256を受け取ります。配布物には上流の名称 `FilmCraft` が使われています。すでにFilmCraftを使っているPCに同名のアプリがある場合は上書きせず、別の検証環境を使ってください。自分でソースから作る場合は[ビルド手順](../development/build-installer.md)から始めます。

## macOS

1. Appleメニューの「このMacについて」でチップを確認します。Appleシリコンなら `macos-aarch64.dmg`、Intelなら `macos-x86_64.dmg`、どちらでも使う配布物なら `macos-universal.dmg` を選びます。
2. ターミナルで `shasum -a 256` と空白を入力し、FinderからDMGをドラッグしてReturnを押します。表示された値を配布担当のSHA-256と照合します。
3. DMGを開き、中の `FilmCraft.app` を「アプリケーション」にドラッグします。コピー完了後にDMGを取り出し、「アプリケーション」から開きます。
4. 開発元や公証についてmacOSが警告する場合は、表示された文言とファイル名を配布担当に伝え、社内で承認された署名・公証済みの版を受け取ります。

自分のMacでビルドした版を試すときは、アプリを空の専用フォルダーにコピーできます。たとえば `~/Applications/Cutset-Trial/FilmCraft.app` に置いた場合、次のコマンドはデモ案件と専用の設定・自動保存フォルダーで起動します。案件の保存先は編集画面から選べます。

```sh
"$HOME/Applications/Cutset-Trial/FilmCraft.app/Contents/MacOS/FilmCraft" \
  --demo --data-dir "$HOME/Library/Application Support/Cutset-Trial"
```

## Windows

1. 「設定 → システム → バージョン情報」で「システムの種類」を確認し、配布担当が指定したアーキテクチャのMSIを受け取ります。
2. PowerShellの `Get-FileHash -Algorithm SHA256 -Path "受け取ったファイルのパス"` で照合し、MSIを開きます。インストーラで利用者の範囲を選びます。既定は現在のユーザーです。
3. インストール先の `filmcraft.exe` を起動します。スタートメニューのショートカットを作成した場合は、そこからも開けます。セキュリティ警告や管理者承認が出た場合は社内の配布担当に確認します。

通常のインストールには配布用のMSIを使います。`NOT-INSTALLABLE.msi` はインストーラの検査用です。[Windowsのインストール仕様](../../packaging/windows/INSTALLATION.md)

## Linux

配布担当が指定したディストリビューションとCPU向けのパッケージを選びます。`sha256sum ファイル名` で照合し、Debian系の `.deb` またはRPM系の `.rpm` をシステムのソフトウェアインストーラーで開きます。インストール後はアプリ一覧の「FilmCraft」か、端末で `filmcraft` を実行します。

管理者権限を使わずtar版を試す場合は、受け取った `.tar.gz` を空のフォルダーに展開し、展開先の `install.sh` があるフォルダーで `./install.sh` を実行します。標準の導入先は `~/.local` です。端末で見つからない場合は `"$HOME/.local/bin/filmcraft"` で起動します。[Linuxのインストール処理](../../packaging/linux/install.sh)

## FreeBSD

配布担当が指定したCPU向けの `.tar.gz` を受け取り、`sha256 ファイル名` で照合します。試用する場合は空のフォルダーに展開して、展開先の `bin/filmcraft` を実行します。共用PCの `/usr/local` への導入は配布担当が行います。[FreeBSDの配布形式](../../packaging/freebsd/package.sh)

## 更新と取り外し

更新前に案件と元の素材を別の場所にも保存します。新しい版でそのコピーを開き直し、再生と短い書き出しを試してください。旧版と同じ名前のアプリやファイル関連付けがある環境では、配布担当が確認した更新手順を使います。

macOSで専用フォルダーにコピーした試用版は、終了してその `FilmCraft.app` をゴミ箱へ移すと取り外せます。WindowsのMSIは「設定 → アプリ → インストールされているアプリ」、Linuxのdeb・rpmは導入に使ったパッケージ管理ツールから削除します。案件・素材・試用プロファイルは個別に管理します。

## 最初に確認すること

編集画面が開いたら短い動画を読み込み、自分の案件フォルダーに別名で保存します。アプリを閉じ、同じ案件を開き直して素材が再生できることを確かめます。案件を別のPCへ渡すときは元の素材も一緒に渡してください。[最初の案件と素材](project-and-media.md) ・ [最初の編集](timeline-editing.md)

起動できない場合はOS・CPU、ファイル名、配布元が案内した版、エラー文を配布担当に伝えます。社内素材や個人のファイルパスが含まれるログは公開Issueへ貼らず、社内の窓口で共有してください。
