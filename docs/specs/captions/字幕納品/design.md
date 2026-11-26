# 字幕納品の設計（CC-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

納品画面で字幕トラック・言語・焼き込み・サイドカー・埋め込みを選択し、再生確認用の出力方法を表示する。

## データと処理境界

焼き込みは映像合成、サイドカーは独立したタイムコード文字列、埋め込みは媒体の字幕ストリームとして処理する。各経路の対応形式と変換で落ちる属性を示す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/caption_export.rs](../../../../crates/ui-egui/src/panels/caption_export.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
