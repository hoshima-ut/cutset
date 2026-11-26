# 静止フレームの作業・試験（ED-35）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-35`、受入IDは `AC-ED-35`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

番号25を[50,60)に保持し、出力の50〜59すべてが25になることを確認する。60以降の扱いが選んだ挿入方法と一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [frame_hold_options_add_frame_hold_and_hold_segment](../../../../crates/engine/src/clip_ops_tests.rs#L474) は <code>clip.frameHoldOptions</code> を呼ぶ。
- [keyframes_on_a_frame_hold_go_where_the_playhead_is](../../../../crates/engine/src/tests.rs#L526) は <code>clip.frameHoldOptions</code> を呼ぶ。
- [values_changed_on_a_frame_hold_are_keyed_where_the_playhead_is](../../../../crates/engine/src/tests.rs#L551) は <code>clip.frameHoldOptions</code> を呼ぶ。
