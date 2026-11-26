# 字幕と文字データの設計（IO-46）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象字幕と言語を選択し、焼き込み・サイドカー・埋込みのうち形式が扱える方法を選ぶ。

## データと処理境界

字幕キューの半開時間範囲、文字列、改行、言語、出力範囲からの時刻起点を変換器に渡す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/caption_export.rs](../../../../crates/ui-egui/src/panels/caption_export.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
