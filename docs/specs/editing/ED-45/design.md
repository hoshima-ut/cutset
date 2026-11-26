# ED-45 操作履歴 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

履歴で操作名と対象を確認し、最後の編集から順にUndo/Redoする。診断イベントを別表示で絞り込める。

## データと処理境界

案件編集は変更前後を戻せる取引として登録する。読み取りや試聴のイベントは時刻と対象を記録してもUndo単位を増やさない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/history_tests.rs](../../../../crates/engine/src/history_tests.rs)、[crates/engine/src/lib.rs](../../../../crates/engine/src/lib.rs)。

確認した関数：[undo](../../../../crates/engine/src/lib.rs)。履歴のプロジェクトを復元し、直前の内容・操作名・由来をRedoへ移す。操作元の保存に試験がある。複数のAI採用を一回で戻すには、その確定単位を別に検証する。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>edit.redo</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.undo</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
