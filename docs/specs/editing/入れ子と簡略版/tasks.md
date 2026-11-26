# 入れ子と簡略版の作業・試験（ED-24）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-24`、受入IDは `AC-ED-24`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

子の[10,30)を親の50に配置し、子12の画を差し替える。親52で新しい画が見え、展開コピーだけの編集は子へ戻らない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [reveal_nested_sequence_opens_it_at_the_matching_frame](../../../../crates/engine/src/keyboard_tests.rs#L372) は <code>sequence.revealNested</code> を呼ぶ。
- [make_subsequence_from_in_out_and_from_selection](../../../../crates/engine/src/sequence_tools_tests.rs#L346) は <code>sequence.makeSubsequence</code> を呼ぶ。
- [match_frame_on_a_nest_loads_the_nested_sequence_at_the_frame_it_shows](../../../../crates/engine/src/nest_editing_tests.rs#L165) は <code>clip.nest</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/nest_fidelity_tests.rs](../../../../crates/engine/src/nest_fidelity_tests.rs)。
