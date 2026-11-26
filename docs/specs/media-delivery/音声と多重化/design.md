# 音声と多重化の設計（IO-43）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

出力の映像・音声の有無、トラック構成、チャンネル順とコンテナを選び、音声ルーティングを確認する。

## データと処理境界

入力チャンネルと出力チャンネルの対応表、サンプルレート、ダウンミックス係数をジョブに渡す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/export/src/surround_tests.rs](../../../../crates/export/src/surround_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
