# キーフレームの操作の作業・試験（FX-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-06`、受入IDは `AC-FX-06`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

位置と不透明度のキーをともにフレーム12に置き、位置だけ13へ移す。保存再開後に位置は13、不透明度は12。Undo可能な同一セッションでは移動も差し戻せる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [add_and_delete_keyframe_undo_redo_and_need_a_sequence](../../../../crates/engine/src/tests.rs#L462) は <code>effects.deleteKeyframe</code> を呼ぶ。
- [add_keyframe_at_the_out_point_stays_there_and_the_replies_say_what_happened](../../../../crates/engine/src/tests.rs#L401) は <code>effects.addKeyframe</code> を呼ぶ。
- [add_keyframe_toggles_the_keyframe_at_the_playhead](../../../../crates/engine/src/tests.rs#L353) は <code>effects.addKeyframe</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/keyframe_move.rs](../../../../crates/engine/src/keyframe_move.rs)。
