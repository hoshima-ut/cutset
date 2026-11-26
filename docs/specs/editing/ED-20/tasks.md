# ED-20 除去とギャップ — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-20`、受入IDは `AC-ED-20`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

[20,32)を削除する。Liftは32の直前まで空白、Extractでは元の32番が20に現れる。Undo後の配置順とロックBGMを比較する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [ripple_delete_of_a_j_cut_clip_closes_one_gap](../../../../crates/engine/src/ripple_delete_tests.rs#L39) は <code>edit.rippleDelete</code> を呼ぶ。
- [ripple_delete_of_a_straight_cut_clip_is_unchanged](../../../../crates/engine/src/ripple_delete_tests.rs#L91) は <code>edit.rippleDelete</code> を呼ぶ。
- [ripple_delete_of_an_l_cut_clip_keeps_the_next_clip_in_sync](../../../../crates/engine/src/ripple_delete_tests.rs#L71) は <code>edit.rippleDelete</code> を呼ぶ。
- 対応を確認したテスト：[extract_and_lift](../../../../crates/edit/src/tests.rs)。
