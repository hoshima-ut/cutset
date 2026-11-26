# 試聴品質の設計（UI-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

再生中を1/4、停止時を原寸にし、同一区間を再生・停止する。選択解像度と欠落フレーム数を表示する。

## データと処理境界

再生・停止の解像度はモニター設定、出力寸法はエクスポート設定とする。計測値には観測区間と実際に表示したフレーム数を添える。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor_view.rs](../../../../crates/ui-egui/src/panels/monitor_view.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
