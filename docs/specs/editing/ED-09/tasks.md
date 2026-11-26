# ED-09 シーケンス作成 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-09`、受入IDは `AC-ED-09`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

1920×1080・24fps素材から1080×1920・25fpsのシーケンスを作る。保存再開後も両方の設定がそれぞれ元どおり読める。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [new_sequence_from_clip_bin_from_selection_and_offline_file](../../../../crates/engine/src/clip_ops_tests.rs#L290) は <code>file.newSequenceFromClip</code> を呼ぶ。
- [native_menu_follows_undo_and_redo_availability](../../../../crates/ui-egui/src/app/commands.rs#L70) は <code>file.newSequence</code> を呼ぶ。
- [new_sequence_from_clip_carries_the_pixel_aspect](../../../../crates/engine/src/par_tests.rs#L49) は <code>file.newSequence</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/sequence_tools_tests.rs](../../../../crates/engine/src/sequence_tools_tests.rs)。
