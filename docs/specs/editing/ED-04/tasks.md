# ED-04 素材からの範囲選択 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-04`、受入IDは `AC-ED-04`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

映像・音声付き素材の[10,30)を映像だけで配置するとV1に20フレームが増え、A1は空のまま。試聴だけなら配置は増えない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [source_clips_are_remembered_and_closed_in_turn](../../../../crates/engine/src/source_monitor.rs#L359) は <code>source.close</code> を呼ぶ。
- [timeline_clip_opens_in_source_at_the_matching_frame](../../../../crates/engine/src/source_monitor.rs#L380) は <code>source.open</code> を呼ぶ。
- [caption_track_follows_sync_locked_insert](../../../../crates/engine/src/captions/tests.rs#L101) は <code>source.open</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。
