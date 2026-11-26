# ED-08 入力方式の設定 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

使用する配列とキーセットを選び、操作を検索して割当を変更し、タイムラインと字幕入力欄で試す。

## データと処理境界

保存する命令IDと修飾キーをOS表記へ変換し、パネルとテキスト編集の優先順位を定義する。キーボードだけで割当解除・復元できる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/shortcuts.rs](../../../../crates/engine/src/shortcuts.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
