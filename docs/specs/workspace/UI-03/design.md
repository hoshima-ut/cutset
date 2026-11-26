# UI-03 モニター操作の配置 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材モニターのボタン編集で挿入とマーカーを並べ、仮表示で順序を確認して確定する。完成モニターは別に設定する。

## データと処理境界

各モニターのボタンID配列をユーザーの作業面に保存する。編集ダイアログが編集中の配列を所有する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
