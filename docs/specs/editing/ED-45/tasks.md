# ED-45 操作履歴 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-45`、受入IDは `AC-ED-45`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

分割、移動、字幕訂正を実施後に3回Undoする。配置数・位置・字幕が逆順で戻り、途中の診断表示はUndo回数に含まれない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [delete_redoable_actions_forgets_the_undone_steps_only](../../../../crates/engine/src/history_tests.rs#L22) は <code>edit.redo</code> を呼ぶ。
- [undo_steps_keep_the_command_that_made_them](../../../../crates/engine/src/history_tests.rs#L84) は <code>edit.undo</code> を呼ぶ。
- [clear_history_forgets_every_step_and_keeps_the_project](../../../../crates/engine/src/history_tests.rs#L45) は <code>edit.undo</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/lib.rs](../../../../crates/engine/src/lib.rs)。
- 対応を確認したテスト：[undo_steps_keep_the_command_that_made_them](../../../../crates/engine/src/history_tests.rs)。

デモ案件でマーカー追加・Undo・Redoを実行し、操作前後のシーケンス全体を照合済み。 [実行記録](../../../verification/marker-history.md)
