# IO-44 色・画質・重ね表示 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

納品版ごとに画質、色変換、焼き込みの有無を選び、変換後のプレビューを確認する。

## データと処理境界

作業色空間から出力色空間への変換、符号化タグ、焼き込みレイヤーを同一ジョブの設定として固定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/export/src/hdr_tests.rs](../../../../crates/export/src/hdr_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
