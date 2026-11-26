# 取り込み先の選択の設計（UI-05）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材をトレイに追加し、参照またはコピー、並び順、保存先ビンを確認して取り込む。

## データと処理境界

取り込み要求には案件ID、宛先ビンID、順序付きの素材一覧、転送方法を持たせる。検査後に生成した素材IDを同じ順で返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/import_mode.rs](../../../../crates/ui-egui/src/panels/import_mode.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
