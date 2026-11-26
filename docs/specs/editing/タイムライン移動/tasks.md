# タイムライン移動の作業・試験（ED-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-10`、受入IDは `AC-ED-10`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同名シーケンスを2案件に作り、片方の検索結果から次の編集点へ移動する。切り替え先の別案件では元の位置を維持する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [normalize_mix_track_hits_the_target_peak](../../../../crates/engine/src/sequence_extras/tests.rs#L128) は <code>sequence.normalizeMixTrack</code> を呼ぶ。
- [selection_follows_playhead](../../../../crates/engine/src/sequence_tools_tests.rs#L800) は <code>sequence.selectionFollowsPlayhead</code> を呼ぶ。
- [through_edits_show_and_join](../../../../crates/engine/src/sequence_tools_tests.rs#L119) は <code>sequence.throughEdits</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/timeline.rs](../../../../crates/ui-egui/src/panels/timeline.rs)。
