# IO-51 選択シーケンスの取り込み — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

別案件を開いて取り込むシーケンスを選び、依存するネスト・ビン・素材と同名項目を確認する。

## データと処理境界

依存グラフを辿り、元IDと受入案件内のID対応を作る。同名ではなく内容と参照関係を照合して再利用を決める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_tools.rs](../../../../crates/engine/src/project_tools.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
