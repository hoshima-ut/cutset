# 一覧パネルへの移動の設計（MN-26）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

配置表・マーカー一覧を開き、条件で絞って対象行を選ぶ。行の種別に応じて配置、空白、時刻へ移動する。

## データと処理境界

一覧行は対象シーケンスと配置またはマーカーのIDを持つ。空白行は前後の配置と時間範囲で現在の位置を再解決する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/sequence_inspect_tests.rs](../../../../crates/engine/src/sequence_inspect_tests.rs)、[crates/ui-egui/src/panels/markers_panel.rs](../../../../crates/ui-egui/src/panels/markers_panel.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
