# UI-04 キーの割当と競合 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-04`、受入IDは `AC-UI-04`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

字幕入力欄でDeleteを押すと文字だけが消え、同じキーをタイムラインで押すと対象配置に作用する。競合解消を取り消すと両操作の割当が元に戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [assign_reassigns_conflicts_and_undoes](../../../../crates/engine/src/shortcuts_tests.rs#L75) は <code>shortcuts.conflicts</code> を呼ぶ。
- [clear_close_sequence_also_clears_file_close](../../../../crates/engine/src/shortcuts_tests.rs#L117) は <code>shortcuts.clear</code> を呼ぶ。
- [clear_new_bin_frees_cmd_b_in_the_project_panel_too](../../../../crates/engine/src/shortcuts_tests.rs#L137) は <code>shortcuts.clear</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/shortcuts.rs](../../../../crates/engine/src/shortcuts.rs)。
- 対応を確認したテスト：[assign_reassigns_conflicts_and_undoes](../../../../crates/engine/src/shortcuts_tests.rs)。
