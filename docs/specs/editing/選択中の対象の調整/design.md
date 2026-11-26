# 選択中の対象の調整の設計（ED-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

共通属性を持つ複数配置を選び、対象数と元の値を確認して新しい値を一括適用する。

## データと処理境界

属性の所有者が素材、配置、効果インスタンスのどれかを指定し、対応するID集合を一つの更新要求にまとめる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/effect_controls.rs](../../../../crates/ui-egui/src/panels/effect_controls.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
