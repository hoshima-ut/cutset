# 音声フェードの作業・試験（AU-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-12`、受入IDは `AC-AU-12`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ位相・同じ振幅の音を交差させる。中点で線形は各0.5、等パワーは各約0.707。音を足した結果と、片側を無音にした際の測定値を比較する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [default_audio_transition_is_used_by_apply](../../../../crates/engine/src/mixer_tests.rs#L403) は <code>sequence.applyAudioTransition</code> を呼ぶ。
- [apply_video_transition_goes_to_the_selection_not_the_playhead](../../../../crates/engine/src/sequence_extras/tests.rs#L87) は <code>sequence.applyAudioTransition</code> を呼ぶ。
- [default_transition_durations](../../../../crates/engine/src/settings_tests.rs#L351) は <code>sequence.applyAudioTransition</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/transition_controls.rs](../../../../crates/ui-egui/src/panels/transition_controls.rs)。
