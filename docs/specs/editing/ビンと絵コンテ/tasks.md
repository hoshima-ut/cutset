# ビンと絵コンテの作業・試験（ED-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-03`、受入IDは `AC-ED-03`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

A/B/CをC/A/Bで配置した後、ビンを名前順に戻す。ビンはA/B/C、タイムラインはC/A/Bを保持する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [freeform_stacks_and_arrangements](../../../../crates/engine/src/project_panel_tests.rs#L215) は <code>project.freeform.arrangements</code> を呼ぶ。
- [select_all_in_a_bin_skips_closed_bins_and_other_bins](../../../../crates/engine/src/project_panel_tests.rs#L310) は <code>project.selectAll</code> を呼ぶ。
- [select_all_rejects_bad_bins_without_touching_the_selection](../../../../crates/engine/src/project_panel_tests.rs#L359) は <code>project.selectAll</code> を呼ぶ。
