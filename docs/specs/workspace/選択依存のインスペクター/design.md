# 選択依存のインスペクターの設計（UI-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

配置を複数選択し、値が揃う属性と混在する属性を確認する。変更前に適用可能な対象数を表示する。

## データと処理境界

対象の種類・配置ID・素材ID・ロック状態から編集可能属性の共通集合を作る。混在値には専用の表示状態を使う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/effect_controls.rs](../../../../crates/ui-egui/src/panels/effect_controls.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
