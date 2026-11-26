# レイアウトの管理の設計（MN-25）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

パネル配置に名前を付けて保存し、別の配置へ切り替える。画面外の浮動パネルもリセットから回収できる。

## データと処理境界

パネルID、ドッキング位置、表示状態とウィンドウ寸法をレイアウトとして保存する。シーケンスの保存履歴とは独立させる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/workspaces.rs](../../../../crates/ui-egui/src/panels/workspaces.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
