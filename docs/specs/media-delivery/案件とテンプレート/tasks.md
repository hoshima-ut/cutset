# 案件とテンプレートの作業・試験（IO-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-01`、受入IDは `AC-IO-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

空の案件Aと、ビン2個・シーケンス1本のひな型から案件Bを作る。Bのビンを改名しても、Aとひな型を再度開いた結果が変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [close_commands_and_templates](../../../../crates/engine/src/project_tools/tests.rs#L165) は <code>file.newProjectFromTemplate</code> を呼ぶ。
- [deleting_media_used_on_the_timeline_makes_it_offline](../../../../crates/engine/src/project_tools/tests.rs#L609) は <code>file.newProject</code> を呼ぶ。
- [new_project_answers_with_its_name_and_revision](../../../../crates/engine/src/file_tests.rs#L114) は <code>file.newProject</code> を呼ぶ。
