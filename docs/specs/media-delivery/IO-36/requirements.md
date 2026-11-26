# IO-36 版指定レビュー — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

共有版に紐づく範囲コメントと回答を同期し、旧版からも元の画を開ける。

## 受入条件

二つの版の同一タイムコードに別々のコメントを付け、それぞれの返信から正しい版の画と会話に戻れる。

## 例外と復旧

閲覧権が失効したら新規取得を止める。旧版へのアクセスが無い場合はその旨を表示し、現行版へ黙って移動しない。

## 参照資料と確認項目

- [A698](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/about-frameio.html)　26系でV4とLegacyの表示を照合し、利用アカウントとパネルの正しい組み合わせを選べるか確認する。（公開手順）
- [A699](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/upload-media-to-frameio.html)　検証フォルダーへ一つの素材を送信し、元ファイルの尺とFrame.io上のプレビュー時間を照合する。（公開手順）
- [A700](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/add-comments-on-shared-projects.html)　同じ版の異なる2フレームに指摘を書き、投稿者とタイムコードを編集者側で識別できるか確認する。（公開手順）
- [A701](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/add-collaborators-using-the-frameio-panel.html)　共有先とメールアドレスを選び、検証用の招待が意図したFrame.io案件のみに届くか試す。（公開手順）
- [A702](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/remove-collaborators-using-the-frameio-panel.html)　検証参加者を解除し、共有案件の他の共同作業者まで外れないことを一覧で確認する。（公開手順）
- [A703](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/share-for-review-with-frame-io.html)　特定版のレビューリンクを別ユーザーで開き、視聴・コメント権限と実際に見える版を照合する。（公開手順）
- [A704](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/import-comments-as-markers.html)　Legacyでは取り込んだマーカーの時刻を、V4では同期したコメントの対象版を元の指摘と見比べる。（公開手順）
- [A705](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/integrate-adobe-workfront-with-frameio.html)　検証用Workfront案件のレビュー依頼をFrame.ioで開き、対象の素材版と戻った承認状態を照合する。（公開手順）
- [A706](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/share-for-review-using-frame-io/invite-collaborators-to-co-edit-a-project.html)　確認専用参加者と共同編集者を別に招き、動画への指摘とシーケンス編集で使う権限を判別する。（公開手順）
