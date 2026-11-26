# ED-19 分割と再結合 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-19`、受入IDは `AC-ED-19`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

素材[100,150)を20フレーム目で分割し、[100,120)と[120,150)を得る。結合後の尺は50、境界付近の番号は119→120となる。

- QA-01　25fps、素材内区間[100,150)の50フレームをシーケンス先頭に配置し、20フレーム目の境界で分割。 期待結果：素材範囲は[100,120)と[120,150)。出力は50フレーム、映る番号は100から149まで順に各一回。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [add_edit_cuts_only_the_selected_clips](../../../../crates/engine/src/clip_ops_tests.rs#L1130) は <code>sequence.addEdit</code> を呼ぶ。
- [a_regular_trim_that_opens_a_gap_drops_the_crossfade](../../../../crates/engine/src/clip_ops_tests.rs#L1046) は <code>timeline.razor</code> を呼ぶ。
- [reveal_nested_and_join_through_edits_are_enabled_only_when_they_can_act](../../../../crates/engine/src/sequence_tools_tests.rs#L957) は <code>sequence.joinThroughEdits</code> を呼ぶ。
- 対応を確認したテスト：[razor_keeps_content_continuous](../../../../crates/edit/src/tests.rs)。
