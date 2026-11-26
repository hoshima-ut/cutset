# UI-11 文字・値の入力 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

数値欄をドラッグして仮値を見た後、直接入力で微調整する。文字欄の変換中はEnterとEscをIMEへ渡す。

## データと処理境界

ドラッグ開始値・仮値・確定値を区別し、単位と上下限を表示する。確定時に一回だけ対象IDと値を編集命令へ渡す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/graphics/ime.rs](../../../../crates/ui-egui/src/panels/graphics/ime.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
