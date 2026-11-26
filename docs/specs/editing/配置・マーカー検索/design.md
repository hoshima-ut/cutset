# 配置・マーカー検索の設計（ED-22）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

検索欄で配置名または注記を絞り、結果に表示された行・配置・時刻を選んでジャンプする。

## データと処理境界

結果行には所属案件、素材またはシーケンス、配置IDと元時刻を返す。素材の注記が複数配置に現れる場合は使用箇所を個別に返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/sequence_inspect_tests.rs](../../../../crates/engine/src/sequence_inspect_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
