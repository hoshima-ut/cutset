# ED-17 サブクリップ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材にIn/Outを付け、サブクリップ名と範囲制限を指定してビンに登録し、別の範囲も作る。

## データと処理境界

別の項目IDから同じ原本IDと素材範囲を参照する。トリムの限界はサブクリップの境界と原本の物理境界で決める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/clip_ops.rs](../../../../crates/engine/src/clip_ops.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
