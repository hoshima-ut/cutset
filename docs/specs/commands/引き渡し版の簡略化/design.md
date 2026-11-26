# 引き渡し版の簡略化の設計（MN-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

簡略化するシーケンスを選び、空トラック・無効配置・マーカー等を個別に選択して結果を別版として作る。

## データと処理境界

新しいシーケンスIDと元版の対応を保存し、除去した種類と件数を返す。残す配置は原本参照を維持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/nest_fidelity_tests.rs](../../../../crates/engine/src/nest_fidelity_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
