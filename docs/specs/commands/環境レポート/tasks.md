# 環境レポートの作業・試験（MN-28）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-MN-28`、受入IDは `AC-MN-28`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

空案件で診断し、利用できない機器を1つ含む構成で試す。読めた項目を確認でき、取消時に出力なし、保存時は選択項目だけが出力される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/project_tools/tests.rs](../../../../crates/engine/src/project_tools/tests.rs)。
- 対応を確認したテスト：[system_report_lists_the_build](../../../../crates/engine/src/project_tools/tests.rs)。
