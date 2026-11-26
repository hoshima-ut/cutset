# GR-08 テンプレート交換 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

メディア枠ごとに置換素材を選び、フィット・クロップの結果を確認する。公開するデータ項目と同梱可能な素材を選んで書き出す。

## データと処理境界

枠ID、受理する媒体種別、縦横比処理、データ型と必須項目をテンプレートに記録する。外部依存は相対参照または再リンク情報として列挙する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
