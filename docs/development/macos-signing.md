# 初めてCutsetのMac版を社内配布する

会社のMac・iOSアプリを管理する担当者に「会社のApple Developer Programに加入していますか。Developer ID Applicationで署名できるMacはありますか」と確認します。証明書は配布担当が管理します。編集者はDMGを受け取って使えます。GitHub上のリポジトリの所有者とAppleの署名チームは別に選べます。

| 会社の状況 | 最初の作業 |
| --- | --- |
| 署名できるMacがある | そのMacでCutsetを取得し、下の「公証の設定」に進みます。秘密鍵のコピーは不要です。 |
| 会員だが証明書がない | 会社のAccount Holderに以下の証明書発行を依頼します。 |
| 未加入 | 会社を代表して契約できる担当者が通常のApple Developer Programに組織として加入します。Appleは法人情報、D‑U‑N‑S番号、2ファクタ認証などを確認します。年会費の基準は99米ドルで、現地の価格は登録画面に表示されます。 |

この手順はMac App Storeの外でDMGを渡す方式です。Apple Developer Enterprise Programへの加入やApp Storeへの掲載は必要ありません。個人の有料チームでも配布できますが、署名者はその個人になります。会社を配布元として表示する場合は会社のチームを使います。[Appleの登録案内](https://developer.apple.com/jp/programs/enroll) ・ [Developer ID](https://developer.apple.com/developer-id/)

## 加入前に編集者と試す

少人数で操作を評価するだけなら、それぞれのMacで同じコミットを取得し、[Appleシリコンでのビルドと動作確認](../verification/macos-install.md)に従って `--local` を使えます。自分でビルドした版をそのMacで起動する方法です。複数人に同じDMGを渡す段階で、以下の署名・公証を一度行います。

## 証明書を初めて作る

1. 配布担当が使うMacの「キーチェーンアクセス」で「証明書アシスタント」から認証局に証明書を要求し、要求ファイル（CSR）をディスクに保存します。秘密鍵はこのMacに残ります。
2. Account Holderが会社のApple Developerアカウントの「Certificates, Identifiers & Profiles」→「Certificates」→「＋」で **Developer ID Application** を選び、CSRをアップロードします。このDMGは同証明書で署名します。「Developer ID Installer」は署名対象がPKGの場合に使います。
3. 発行した証明書（.cer）をCSRを作ったMacで開きます。キーチェーンアクセスの「自分の証明書」で、証明書を展開すると対応する秘密鍵があることを確認します。次のコマンドに有効な Developer ID Application の行が出たら、その表示名を控えます。

```sh
security find-identity -v -p codesigning
```

[Appleの発行手順と必要な権限](https://developer.apple.com/help/account/certificates/create-developer-id-certificates)

## 公証の設定

署名用MacにXcode Command Line Toolsを用意します。公証に使うApple Accountのアプリ用パスワードを用意し、下記のメールアドレスとTeam IDを自分のチームの値に置き換えます。パスワードはプロンプトに入力します。リポジトリやチャットに入力する作業はありません。

```sh
xcrun notarytool store-credentials cutset-notary \
  --apple-id '担当者のApple Accountのメールアドレス' --team-id '会社のTeam ID'
xcrun notarytool history --keychain-profile cutset-notary
```

認証情報はこのユーザーのキーチェーンに保存されます。配布スクリプトに渡すのはプロファイル名です。[Appleの公証ツール設定例](https://developer.apple.com/documentation/technotes/tn3147-migrating-to-the-latest-notarization-tool)

## DMGを作って渡す

Cutsetのクローン直下で実行します。Appleシリコンのみならターゲットは `aarch64-apple-darwin`、引数は `--arch aarch64` にできます。

```sh
rustup target add aarch64-apple-darwin x86_64-apple-darwin
export MACOS_SIGN_IDENTITY='Developer ID Application: 組織名 (TEAMID)'
export CUTSET_NOTARY_PROFILE=cutset-notary
bash packaging/macos/package.sh --arch universal
```

スクリプトは署名し、成果物をAppleの公証サービスへ送信します。受理後にアプリとDMGへチケットを添付し、Gatekeeperの検査まで通った成果物を `dist/release/` に出します。初回は署名用Macとは異なる社内のMacで、実際の配布経路からDMGを取得し、Applicationsへのコピー、通常起動、既存案件のコピーを開いて保存する操作を確認します。確認後、同じDMGとSHA-256を編集者に配ります。[ビルド手順](build-installer.md) ・ [編集者のインストール手順](../manual/install.md)
