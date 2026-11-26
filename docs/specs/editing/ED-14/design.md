# ED-14 三点・四点編集 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材と完成側にIn/Outを置き、未指定の一点を算出する。両側の尺が異なる場合は優先する範囲・速度変更を選ぶ。

## データと処理境界

素材とシーケンスの異なる時間基準を有理数で変換し、決定した素材範囲、宛先範囲、再生率を適用前に表示する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/source_placement_tests.rs](../../../../crates/engine/src/source_placement_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
