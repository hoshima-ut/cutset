# MN-03 保管パッケージ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

保管メニューで対象シーケンスと除外条件を確認し、収集対象・未解決依存・必要容量の一覧を見て確定する。

## データと処理境界

案件管理処理にはシーケンスID集合と目的地を渡す。確定済みパッケージの一覧は収集成功後に作る。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_manager.rs](../../../../crates/engine/src/project_manager.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
