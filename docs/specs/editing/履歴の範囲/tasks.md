# 履歴の範囲の作業・試験（ED-59）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-59`、受入IDは `AC-ED-59`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

トリム→パネル拡大→Undoでパネルの大きさを維持し、トリムだけが戻る。保存・再起動後は世代を明示選択して以前の状態を開く。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [clear_history_forgets_every_step_and_keeps_the_project](../../../../crates/engine/src/history_tests.rs#L45) は <code>history.clear</code> を呼ぶ。
- [delete_redoable_actions_forgets_the_undone_steps_only](../../../../crates/engine/src/history_tests.rs#L22) は <code>history.deleteRedoable</code> を呼ぶ。
- [history_commands_ignore_unexpected_parameters](../../../../crates/engine/src/history_tests.rs#L131) は <code>history.clear</code> を呼ぶ。
