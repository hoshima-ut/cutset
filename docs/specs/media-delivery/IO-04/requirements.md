# IO-04 取り込み処理 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

原本参照、複製、変換、プロキシ生成を組み合わせ、生成物と元素材の関係を記録する。

## 受入条件

カードからコピーを終えてから取り外し、再起動後の参照先を確認。検証コピーを選んだ場合は照合エラーと完了を区別。

## 例外と復旧

容量不足や照合失敗が起きたファイルは不完全として示し、再開時に未完成データを完成品として参照しない。

## 参照資料と確認項目

- [A177](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/ingest-and-proxy-workflow.html)　原本の取り込みとプロキシ編集を連続して行い、プレビュー切替時に同じフレームと音声が保たれるか確かめる。（公開手順）
- [A178](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/configure-ingest-settings.html)　インジェストのコピー先、トランスコードまたはプロキシ生成設定を切り替え、実際の保存先と生成物を照合する。（公開手順）
- [A188](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/migrate-existing-prelude-workflows-to-premiere.html)　既存のPrelude由来素材を引き継ぎ、ログで指定した採用範囲とコメントをPremiere側でどこまで再利用できるか照合する。（公開手順）
- [A728](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/bring-media-into-the-editing-application.html)　放送素材をカード単位で取り込み、カメラが分割した録画の本数・尺・リール情報を原記録と照合する。（公開手順）
