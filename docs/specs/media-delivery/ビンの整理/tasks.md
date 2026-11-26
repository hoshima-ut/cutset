# ビンの整理の作業・試験（IO-15）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-15`、受入IDは `AC-IO-15`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

A/素材とB/素材に同名動画を一つずつ置く。一方を改名・移動しても、各シーケンスの使用箇所は元の動画を開く。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [bins_rename_nest_and_list](../../../../crates/engine/src/project_panel_tests.rs#L251) は <code>file.newBin</code> を呼ぶ。
- [new_items_land_in_the_given_bin](../../../../crates/engine/src/project_panel_tests.rs#L383) は <code>file.newBin</code> を呼ぶ。
- [select_all_in_a_bin_skips_closed_bins_and_other_bins](../../../../crates/engine/src/project_panel_tests.rs#L310) は <code>file.newBin</code> を呼ぶ。
