# 原本の解釈設定の設計（MN-31）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材のプロパティから解釈設定を開き、検出値・上書き値・反映先の使用箇所を確認する。

## データと処理境界

メニューは素材項目に対する操作を発行する。配置単体の速度変更とは異なる対象として履歴とプレビューを更新する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/par_tests.rs](../../../../crates/engine/src/par_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
