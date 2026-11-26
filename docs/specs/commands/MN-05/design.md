# MN-05 交換データの出力 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

書き出しメニューを開いた時点の対象を表示し、素材情報の受け渡しとタイムライン構造の交換から適合する形式を選ぶ。

## データと処理境界

選択種別、対象ID、範囲と交換形式を変換器へ渡す。出力実行直前に対象が存在し形式が扱えることを確認する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/interchange_export.rs](../../../../crates/ui-egui/src/panels/interchange_export.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
