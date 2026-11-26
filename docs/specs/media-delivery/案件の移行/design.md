# 案件の移行の設計（IO-31）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

案件を開く際に形式と版を調べ、変換が必要なら出力先と変換対象を確認する。

## データと処理境界

読込可能な形式だけを版ごとの変換器に渡し、元スキーマ・出力版・扱えない要素を変換結果に残す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/interchange.rs](../../../../crates/engine/src/interchange.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
