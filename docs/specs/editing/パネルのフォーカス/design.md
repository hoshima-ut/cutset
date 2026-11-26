# パネルのフォーカスの設計（ED-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

パネルを選択するとフォーカス枠と操作対象を示す。レイアウト復元後は存在する直近パネルへ戻す。

## データと処理境界

ドックの位置とは別にパネルIDを追跡する。キーは選択中のウィジェットからパネル、アプリの順に処理する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/workspaces.rs](../../../../crates/ui-egui/src/panels/workspaces.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
