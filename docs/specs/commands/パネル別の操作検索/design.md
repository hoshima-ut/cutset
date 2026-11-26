# パネル別の操作検索の設計（MN-35）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

コマンド検索で現在のパネル・選択に使える操作を表示し、割当キーまたは同じ検索結果から実行する。

## データと処理境界

検索結果は操作IDと有効理由・無効理由、ショートカットを返す。実行直前に最新の選択コンテキストで可否を再評価する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/menu_dialogs.rs](../../../../crates/ui-egui/src/panels/menu_dialogs.rs)、[crates/engine/src/keyboard.rs](../../../../crates/engine/src/keyboard.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
