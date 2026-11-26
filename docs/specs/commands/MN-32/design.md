# MN-32 素材一覧の表示切替 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象の素材パネルでリスト・カード等の表示を選ぶ。切替後も選択した行と同じ素材を見つけられるようにする。

## データと処理境界

表示方法と並び順はパネルの状態として扱い、選択は素材IDで保持する。素材所属やタイムラインの配置には書き込まない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_panel.rs](../../../../crates/engine/src/project_panel.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
