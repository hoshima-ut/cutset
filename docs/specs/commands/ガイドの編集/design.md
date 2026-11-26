# ガイドの編集の設計（MN-23）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

モニターのガイドに水平・垂直、座標または比率、表示色を設定して追加する。固定時は位置操作を無効にする。

## データと処理境界

ガイドを表示座標から映像座標へ変換し、ズームとパンに追従させる。モニター描画のみに使用する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor_view.rs](../../../../crates/ui-egui/src/panels/monitor_view.rs)。

確認した関数：[guides](../../../../crates/ui-egui/src/panels/monitor_view.rs)。モニター上のガイドを扱い、定規からの操作を含むUI試験がある。ガイドの単位・個別ロック・書き出し画像への非表示は各条件で照合する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
