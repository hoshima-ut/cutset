# UI-08 作業面の保存 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

パネルを移動・分離し、作業面に名前を付けて保存する。復元時に接続中の画面へ配置を割り当てる。

## データと処理境界

ドック構造、浮動パネルの位置・寸法、最後のアクティブタブを表示設定として扱い、案件編集履歴から分離する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/workspaces.rs](../../../../crates/ui-egui/src/panels/workspaces.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
