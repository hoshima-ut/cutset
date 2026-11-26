# ED-21 配置の置換と属性 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-21`、受入IDは `AC-ED-21`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

20フレームの置換で宛先開始と終端を維持し、選択した不透明度だけを継承する。Undoで元の素材が同じフレームから再生される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [replace_from_bin_keeps_the_source_in_on_request](../../../../crates/engine/src/clip_ops_tests.rs#L757) は <code>clip.replaceFromBin</code> を呼ぶ。
- [replace_from_source_match_frame_on_a_reversed_clip](../../../../crates/engine/src/clip_ops_tests.rs#L731) は <code>clip.replaceFromSourceMatchFrame</code> を呼ぶ。
- [replace_with_clip_from_source_match_frame_and_bin](../../../../crates/engine/src/clip_ops_tests.rs#L694) は <code>clip.replaceFromBin</code> を呼ぶ。
