# ED-58 ショット・補正前後の比較 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

比較の基準フレームを固定し、現在位置との並列表示または同じフレームの補正前後表示を選ぶ。

## データと処理境界

基準の版・時刻と評価する処理段階を保持し、現在の再生位置・分割線の表示位置から独立させる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
