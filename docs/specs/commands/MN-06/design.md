# MN-06 字幕ファイルの出力 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

字幕トラックを選び、言語、書き出し形式、範囲を確かめて保存する。ファイル名の確認時に対象キュー数を表示する。

## データと処理境界

対象トラックIDと言語、シーケンス範囲を字幕変換器に渡し、対象範囲外・別言語のキューを除外する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/caption_export.rs](../../../../crates/ui-egui/src/panels/caption_export.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
