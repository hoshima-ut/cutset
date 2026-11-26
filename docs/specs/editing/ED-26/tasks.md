# ED-26 端のトリム — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-26`、受入IDは `AC-ED-26`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

素材[10,38)を長さ40の原本から使い、末尾を+3指定する。実差分は+2、素材終端40、次の離れた配置の開始位置は同じ。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [trim_delta_stops_at_the_end_of_the_media](../../../../crates/engine/src/trim_tests.rs#L476) は <code>timeline.trim</code> を呼ぶ。
- [trim_steps_record_their_trim_kind](../../../../crates/engine/src/trim_tests.rs#L307) は <code>timeline.trim</code> を呼ぶ。
- [a_regular_trim_that_opens_a_gap_drops_the_crossfade](../../../../crates/engine/src/clip_ops_tests.rs#L1046) は <code>timeline.trim</code> を呼ぶ。
- 対応を確認したテスト：[regular_trim_respects_neighbours_and_handles](../../../../crates/edit/src/tests.rs)。
