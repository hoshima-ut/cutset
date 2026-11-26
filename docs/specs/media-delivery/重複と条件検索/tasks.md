# 重複と条件検索の作業・試験（IO-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-16`、受入IDは `AC-IO-16`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同一原本の参照2件と、同名別原本1件を用意する。統合後は2素材が残り、3つの既存配置はそれぞれの正しい画を表示する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [remove_unused_and_consolidate_duplicates](../../../../crates/engine/src/clip_ops_tests.rs#L202) は <code>edit.consolidateDuplicates</code> を呼ぶ。
- [consolidate_keeps_counting_leaders_with_distinct_source_rates](../../../../crates/engine/src/clip_ops_tests.rs#L263) は <code>edit.consolidateDuplicates</code> を呼ぶ。
- [search_bins_update_live](../../../../crates/engine/src/project_tools/tests.rs#L98) は <code>project.deleteSearchBin</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/media_pool.rs](../../../../crates/engine/src/media_pool.rs)。
