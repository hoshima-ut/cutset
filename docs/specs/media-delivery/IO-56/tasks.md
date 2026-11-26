# IO-56 素材の収集と保管 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-56`、受入IDは `AC-IO-56`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同名の別素材2本と未使用素材1本を用意する。必要な2本だけを収集し、元ストレージを外して別ルートから案件と両方の画を再現できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [collect_files_copies_used_media_and_opens](../../../../crates/engine/src/project_manager_tests.rs#L47) は <code>file.projectManager</code> を呼ぶ。
- [consolidate_trims_to_used_ranges_with_handles](../../../../crates/engine/src/project_manager_tests.rs#L76) は <code>file.projectManager</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/project_manager.rs](../../../../crates/engine/src/project_manager.rs)。
