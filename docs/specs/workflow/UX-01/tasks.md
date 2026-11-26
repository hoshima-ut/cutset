# UX-01 編集命令の共通化 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UX-01`、受入IDは `AC-UX-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ案件のコピー5個でBの終端を1フレーム詰める。経路ごとの配置ID、尺、後続位置とUndo後の内容を比較する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/automation/src/server/tests.rs](../../../../crates/automation/src/server/tests.rs)。
- 関連する既存テストモジュール：[crates/engine/src/lib.rs](../../../../crates/engine/src/lib.rs)。
- 対応を確認したテスト：[clip_commands_take_explicit_clips_without_a_selection](../../../../crates/engine/src/explicit_targets_tests.rs)。
