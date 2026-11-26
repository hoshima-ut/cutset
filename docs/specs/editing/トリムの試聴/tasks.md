# トリムの試聴の作業・試験（ED-32）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-32`、受入IDは `AC-ED-32`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

映像境界50・音声境界47で音声端だけ+1する。音声48、映像50となり、元に戻すと47に一回で戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [extend_previous_and_next_edit_roll_cuts_to_the_playhead](../../../../crates/engine/src/keyboard_tests.rs#L138) は <code>trim.extendNextEdit</code> を呼ぶ。
- [apply_default_transitions_to_selected_clips](../../../../crates/engine/src/sequence_extras/tests.rs#L61) は <code>trim.applyDefaultTransition</code> を呼ぶ。
- [extend_to_playhead_moves_each_unequal_out_point_to_the_playhead](../../../../crates/engine/src/trim_tests.rs#L419) は <code>trim.extendToPlayhead</code> を呼ぶ。
