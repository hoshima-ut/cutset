# IO-06 カメラRAW — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

RAWデコーダーと追加コンポーネントの可用性を調べ、解釈値を素材ごとに保存する。

## 受入条件

同一のBRAWをプラグイン有無の2環境に取り込み、未導入の依存とファイル破損を区別する。

## 例外と復旧

依存するデコーダーが無い端末では該当素材を保留にする。保存済みの解釈値を維持して別端末へ渡せる。

## 参照資料と確認項目

- [A126](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/blackmagic-raw-support.html)　BRAWテスト素材で組み込み機能または外部コンポーネントの要否を対象26系で照合し、デコード可否を記録する。（26系公式記事ではBlackmagic Design製プラグインが依存条件）
