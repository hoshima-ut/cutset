# IO-32 プレビューの計算 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象範囲を指定して生成し、再生可能な区間を表示する。後から指定範囲だけの削除・再生成を選べる。

## データと処理境界

レンダー結果をシーケンス版、半開時間範囲、効果・素材・出力設定に結び付け、依存関係が変わった区間を無効化する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/previews.rs](../../../../crates/engine/src/previews.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.deleteRenderFiles</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.deleteRenderFilesInToOut</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.renderAudio</code> | <code>{"wait":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.renderBar</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.renderEffectsInToOut</code> | <code>{"wait":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.renderInToOut</code> | <code>{"wait":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.renderSelection</code> | <code>{"wait":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
