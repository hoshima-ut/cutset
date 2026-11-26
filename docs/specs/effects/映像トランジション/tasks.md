# 映像トランジションの作業・試験（FX-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-16`、受入IDは `AC-FX-16`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

境界100で20フレームの中央揃えを置く。遷移区間は[90,110)。後続素材の頭側余長を4に減らすと、追加で必要な6フレームが表示される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [apply_video_transition_goes_to_the_selection_not_the_playhead](../../../../crates/engine/src/sequence_extras/tests.rs#L87) は <code>sequence.applyVideoTransition</code> を呼ぶ。
- [a_regular_trim_that_opens_a_gap_drops_the_crossfade](../../../../crates/engine/src/clip_ops_tests.rs#L1046) は <code>sequence.applyVideoTransition</code> を呼ぶ。
- [speed_duration_moves_fade_out_to_the_new_clip_end](../../../../crates/engine/src/clip_ops_tests.rs#L1022) は <code>sequence.applyVideoTransition</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/transition_controls.rs](../../../../crates/ui-egui/src/panels/transition_controls.rs)。
