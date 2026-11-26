# IO-37 共有素材・利用権 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

共有ライブラリやボードの選択素材をローカルに登録し、試用と利用許諾済みを区別する。

## 受入条件

試用素材と利用権取得済み素材の状態を区別し、外部アカウント未接続でも既存のローカル素材を扱えるよう確認。

## 例外と復旧

期限切れや未認証では新規取得や許諾確認を保留する。既に利用可能なローカル素材の通常編集を妨げない。

## 参照資料と確認項目

- [A127](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-media-from-adobe-firefly.html)　Fireflyから1件送信し、受け側で追加された素材と元の生成結果が対応し、手元で再編集できるか確認する。（26.0でFirefly Boardsからデスクトップへ送信。サービス条件を個別照合）
- [A128](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-media-from-firefly-boards.html)　ボード上で選択した3素材を送信し、対応版で作られたシーケンスの順序・個数を選択時と照合する。（26.0でボードから送信、選択順にシーケンス化は26.3）
- [A218](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/use-built-in-adobe-stock.html)　Stockの透かし入りプレビューを選び、ライセンス済みの試験素材への切替時に既存の配置尺と編集点が残るか確認する。（26.2でドラッグ配置、26.3でProjectからのライセンス取得・プレビュー置換）
- [A570](https://helpx.adobe.com/premiere/desktop/add-audio-effects/use-adobe-stock-audio/use-adobe-stock-audio-in-your-project.html)　Stockの音源をプレビューからシーケンスへ置き、既にライセンス済みの試験素材で配置位置と表示を照合する。（公開手順）
- [A571](https://helpx.adobe.com/premiere/desktop/add-audio-effects/use-adobe-stock-audio/about-adobe-stock-audio-licensing-usage-rights-and-audio-quality.html)　試聴用とライセンス済みの音源について表示される利用条件と証跡を開き、対象素材を識別できるか確認する。（公開手順）
- [A707](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/identify-version-of-creative-cloud-libraries-installed.html)　ライブラリ連携のバージョン情報を表示し、アプリ本体のビルド番号と別々に記録する。（公開手順）
- [A708](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/about-creative-cloud-libraries.html)　複数案件から同じ共有グラフィックを探し、ライブラリ名・素材名・サムネイルで識別できるか試す。（公開手順）
- [A709](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/add-a-creative-cloud-library.html)　新しいライブラリを追加して既存と切り替え、新規素材が指定したコレクションに入るか確認する。（公開手順）
- [A710](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/add-looks-to-a-creative-cloud-library.html)　テストクリップのLookを保存して別クリップに適用し、参照画像と色調を見比べる。（公開手順）
- [A711](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/add-assets-from-adobe-stock-to-a-creative-cloud-library.html)　Stockの試用アセットを指定ライブラリに加え、ライセンス取得済み素材との表示差を確認する。（公開手順）
- [A712](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/use-assets-stored-in-creative-cloud-libraries.html)　保存済みのロゴをLibrariesからタイムラインへ配置し、案件を再度開いて大きさと透明部分を確認する。（公開手順）
- [A713](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-creative-cloud-libraries/collaborate-with-other-creative-cloud-users.html)　共有ライブラリへ別ユーザーが追加した素材を、自分の環境で参照できる範囲と時点を記録する。（公開手順）
- [A741](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/unable-to-send-media-from-firefly-to-premiere.html)　Fireflyからの受信に失敗した場合に同一素材を二重に追加せず再試行できる。（障害診断）
- [A747](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/creative-cloud-synced-files-end-of-life-for-premiere.html)　廃止サービスの素材参照を検出し、元ファイルへの再リンクで再開できるか確認する。（Creative Cloud Synced filesの終了情報。現行のLibrary／共同編集とは別）
- [A757](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/video-assets-from-creative-cloud-libraries-broken-between-after-effects-and-premiere.html)　共有ライブラリ由来の映像リンクが切れたとき、参照元と利用先を特定する。（障害診断）
