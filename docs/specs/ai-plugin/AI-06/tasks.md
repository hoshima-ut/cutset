# AI-06 拡張のコマンド契約 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AI-06`、受入IDは `AC-AI-06`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じロック対象にGUIとテストプラグインから短縮案を送る。両方が拒否され、ロック解除・明示確定後はどちらの経路でも一回のUndoで同じ状態に戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [defaults_follow_the_registry_and_the_premiere_audit](../../../../crates/engine/src/shortcuts_tests.rs#L46) は <code>command.list</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/automation/src/server/tests.rs](../../../../crates/automation/src/server/tests.rs)。
