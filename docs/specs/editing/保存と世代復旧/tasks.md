# 保存と世代復旧の作業・試験（ED-46）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-46`、受入IDは `AC-ED-46`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

字幕がA・B・Cの3世代からBを別名保存する。新しいプロセスでBが開き、元のCも残り、両方が同じ原本を参照する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/autosave.rs](../../../../crates/engine/src/autosave.rs)。
- 関連する既存テストモジュール：[crates/engine/src/autosave_tests.rs](../../../../crates/engine/src/autosave_tests.rs)。
- 対応を確認したテスト：[recovery_keeps_original_when_snapshot_write_fails](../../../../crates/engine/src/autosave_tests.rs)。
