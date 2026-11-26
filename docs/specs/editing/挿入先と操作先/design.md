# 挿入先と操作先の設計（ED-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材パッチで入力映像・音声の宛先を選び、別のターゲットトラックを既存編集の対象として選ぶ。

## データと処理境界

素材ストリーム→宛先トラックの対応表と、現在のトラックターゲット集合を操作種別ごとに参照する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/source_placement_tests.rs](../../../../crates/engine/src/source_placement_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
