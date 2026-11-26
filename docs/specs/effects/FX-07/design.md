# FX-07 補間曲線 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

時間グラフで保持・線形・曲線を指定し、座標プロパティでは画面上の経路も調整する。中間時刻をスクラブして値と位置を表示する。

## データと処理境界

キー間の時間補間と、座標の空間補間を別属性で保持する。曲線ハンドルは対応するキーと共に保存し、区間の両端ではキー値を返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/motion_path.rs](../../../../crates/ui-egui/src/panels/motion_path.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
