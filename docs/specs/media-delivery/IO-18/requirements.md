# IO-18 配置の一覧 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

シーケンスの配置を時刻と属性で絞り、該当位置を開く。

## 受入条件

素材名が同じ2カットを時間・トラックで見分け、選んだ方に再生ヘッドが移るか確認。

## 例外と復旧

一覧表示後に配置が削除された場合は行を更新し、同時刻に移動した別配置を開かない。

## 参照資料と確認項目

- [A155](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/navigate-timelines-with-sequence-index.html)　Sequence Indexでオフラインと短いカットを絞り、結果行から正しい位置へ移動しCSVの行とも対応するか確かめる。（26.2でSequence Indexを追加）
