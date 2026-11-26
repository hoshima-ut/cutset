# ED-42 文字から編集 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

文字を選択して検索・試聴・表記修正を行い、映像の除去は別の明示操作から実行する。

## データと処理境界

語の訂正は文字記録の変更。映像編集では選択語の時間境界を外側のフレームに合わせ、対象トラックと削除範囲を提示する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/transcript.rs](../../../../crates/engine/src/transcript.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
