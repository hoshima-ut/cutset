# UI-20 セッション復旧 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-20`、受入IDは `AC-UI-20`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

保存後に字幕を変更して自動保存し、次の保存途中で終了する。元の字幕と復旧可能な新しい字幕を選び分け、各世代の配置・効果を比較する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [recovery_keeps_original_when_worker_has_stopped](../../../../crates/engine/src/autosave.rs#L1169) は <code>file.recover</code> を呼ぶ。
- [crash_recovery_end_to_end](../../../../crates/engine/src/autosave_tests.rs#L159) は <code>file.recover</code> を呼ぶ。
- [recovery_can_retry_after_a_failed_journal_write](../../../../crates/engine/src/autosave_tests.rs#L283) は <code>file.recover</code> を呼ぶ。
