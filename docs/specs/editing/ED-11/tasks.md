# ED-11 トラック管理 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-11`、受入IDは `AC-ED-11`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

V1の青の上にV2の赤を重ねる。V2出力を切ると青になり、V2の高さを変えるだけなら画とA1の信号は同じ。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [delete_tracks_empty_and_specific](../../../../crates/engine/src/sequence_tools_tests.rs#L495) は <code>sequence.deleteTracks</code> を呼ぶ。
- [delete_tracks_removes_caption_tracks](../../../../crates/engine/src/sequence_tools_tests.rs#L519) は <code>sequence.deleteTracks</code> を呼ぶ。
- [add_tracks_places_and_types_them](../../../../crates/engine/src/sequence_tools_tests.rs#L398) は <code>sequence.addTracks</code> を呼ぶ。
