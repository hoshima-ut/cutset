# スライドの作業・試験（ED-30）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-30`、受入IDは `AC-ED-30`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

[0,20)、[20,40)、[40,60)の中央を+3すると各境界は0、23、43、60。中央の先頭・終端の画は移動前と同じ。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [keyboard_slide_keeps_linked_partners_aligned_at_a_neighbour_limit](../../../../crates/engine/src/keyboard_tests.rs#L389) は <code>timeline.slideRight</code> を呼ぶ。
- [nudge_slip_and_slide_the_selection_with_undo](../../../../crates/engine/src/keyboard_tests.rs#L165) は <code>timeline.slideRight</code> を呼ぶ。
- [slide_moves_linked_audio_with_the_video](../../../../crates/engine/src/tests.rs#L144) は <code>timeline.slide</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/slip_tests.rs](../../../../crates/engine/src/slip_tests.rs)。
