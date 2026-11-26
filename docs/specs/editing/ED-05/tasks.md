# ED-05 フレーム送りとシャトル — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-05`、受入IDは `AC-ED-05`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25fps素材の[10,15)でループし、14の次は10に戻る。停止後に2コマ進めて12になり、素材側のIn/Outとクリップ長が同じことを確認する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [clip_volume_keys_and_scrub_toggle](../../../../crates/engine/src/keyboard_tests.rs#L262) は <code>audio.toggleScrubbing</code> を呼ぶ。
- [edit_point_navigation_follows_targets_or_any_track](../../../../crates/engine/src/keyboard_tests.rs#L83) は <code>playhead.nextEditAnyTrack</code> を呼ぶ。
- [select_clip_at_playhead_next_previous_and_go_to_selected_clip](../../../../crates/engine/src/keyboard_tests.rs#L109) は <code>playhead.selectedClipEnd</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。
- 対応を確認したテスト：[j_and_l_shuttle_the_source_both_ways_and_double_the_speed](../../../../crates/ui-egui/tests/it/source_playback_ui.rs)。
