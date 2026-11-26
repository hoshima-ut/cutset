# ED-54 配置表の点検 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

配置一覧にトラック・開始・尺・素材状態を表示し、条件で絞り込んで疑わしい配置へ移動する。

## データと処理境界

行は配置IDに紐付け、表示順とタイムライン順を独立させる。CSVには時刻の単位と元の配置識別情報を含める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/sequence_inspect_tests.rs](../../../../crates/engine/src/sequence_inspect_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
