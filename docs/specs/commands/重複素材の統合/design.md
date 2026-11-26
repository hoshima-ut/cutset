# 重複素材の統合の設計（MN-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

統合メニューで対象のビンや素材を比較し、残す項目と使用中の配置数を確認して適用する。

## データと処理境界

統合候補から代表項目への対応を作り、参照する配置を取引内で付け替える。ビンの統合では名前以外に親階層を照合する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/clip_ops/edit_menu.rs](../../../../crates/engine/src/clip_ops/edit_menu.rs)。

確認した関数：[consolidate_duplicates](../../../../crates/engine/src/clip_ops/edit_menu.rs)。重複した素材参照を統合する。名前の同じ別階層のビン統合や、確認画面で影響する配置を列挙する部分は独立して評価する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
