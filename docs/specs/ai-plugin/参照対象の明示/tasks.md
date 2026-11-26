# 参照対象の明示の作業・試験（AI-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AI-01`、受入IDは `AC-AI-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

素材Aだけを選び、検索では同じ語を含む素材Bも見つかる状態を作る。Bを対象とする変更案は適用されず、Bを個別に許可して初めて該当区間を参照できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/transcript_tests.rs](../../../../crates/engine/src/transcript_tests.rs)。
- 対応を確認したテスト：[generate_inspect_search_and_rename](../../../../crates/engine/src/transcript_tests.rs)。
