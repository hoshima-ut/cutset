# 複数ターゲットの優先順位の設計（ED-53）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

複数トラックをターゲットにし、照合・貼り付け・前後編集点移動ごとに解決される行を操作前に表示する。

## データと処理境界

照合は対象の最上位の可視映像、次編集点は対象行の最も近い境界という順序を仕様とする。貼り付けは最下位の対象トラックを起点に元トラック間隔を保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/explicit_targets_tests.rs](../../../../crates/engine/src/explicit_targets_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
