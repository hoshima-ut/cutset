# トラックとバスの作業・試験（AU-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-06`、受入IDは `AC-AU-06`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

一定の試験音をプリとポストの別バスへ送り、直接音を除いて各バスを測る。元フェーダーを6dB下げるとプリは不変、ポストだけが6dB低下する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [strip_settings_undo_redo_and_inspect](../../../../crates/engine/src/mixer_tests.rs#L69) は <code>mixer.inspect</code> を呼ぶ。
- [clip_automation_spanning_two_clips_writes_both](../../../../crates/engine/src/mixer_tests.rs#L558) は <code>mixer.recordStart</code> を呼ぶ。
- [clip_mixer_latch_and_write_hold_until_stop](../../../../crates/engine/src/mixer_tests.rs#L478) は <code>mixer.recordStart</code> を呼ぶ。
