# 素材の一括配置の作業・試験（ED-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-16`、受入IDは `AC-ED-16`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

長さ10・20・30の素材をC→A→Bで時刻100から並べる。開始位置は100、130、140で、一度のUndoで3配置が消える。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [automate_to_sequence_clamps_transition_to_overlap](../../../../crates/engine/src/project_tools/tests.rs#L533) は <code>clip.automateToSequence</code> を呼ぶ。
- [automate_to_sequence_places_clips_with_overlap_and_transitions](../../../../crates/engine/src/project_tools/tests.rs#L467) は <code>clip.automateToSequence</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/place_items_tests.rs](../../../../crates/engine/src/place_items_tests.rs)。
