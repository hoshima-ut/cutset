# 案件の一部を読み込むの設計（MN-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

ファイル選択で案件を指定するとシーケンス・ビンを展開して選べる。確認後に受入案件の配置先ビンへ追加する。

## データと処理境界

取り込みは元案件の読取専用スナップショットを入力とする。受入先の新IDと依存素材の対応をまとめて確定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/menu_dialogs.rs](../../../../crates/ui-egui/src/panels/menu_dialogs.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
