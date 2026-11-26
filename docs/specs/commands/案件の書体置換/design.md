# 案件の書体置換の設計（MN-22）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

案件で使用中の書体を列挙し、置換対象の本文・字幕とプレビューを比較して確定する。

## データと処理境界

書体の種類・スタイルとテキスト範囲を対応付ける。選択範囲内の参照を一括変更し、本文とキュー時刻を保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/graphics.rs](../../../../crates/ui-egui/src/panels/graphics.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
