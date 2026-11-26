# MN-01 新規作成の対象 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

作成メニューを開くと選択中のビンと作成可能な種類を表示する。作成後は新規項目を選択して名前を変更できる。

## データと処理境界

案件・シーケンス作成はそれぞれ独立した対象を作る。ビンと生成素材の作成には挿入先の親ビンIDを渡す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/menu_dialogs.rs](../../../../crates/ui-egui/src/panels/menu_dialogs.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
