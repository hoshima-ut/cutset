# 入力方式の設定の作業・試験（ED-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-08`、受入IDは `AC-ED-08`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

削除操作を別キーに割り当て、タイムラインで配置を消しUndoする。字幕入力欄で同じ文字を入力しても配置件数は減らない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/shortcuts.rs](../../../../crates/engine/src/shortcuts.rs)。
- 関連する既存テストモジュール：[crates/engine/src/shortcuts_tests.rs](../../../../crates/engine/src/shortcuts_tests.rs)。
