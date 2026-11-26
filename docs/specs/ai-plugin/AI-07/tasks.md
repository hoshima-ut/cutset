# AI-07 推論先と同意 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AI-07`、受入IDは `AC-AI-07`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

字幕テキストだけを許可した案件で、モデルが映像全体を要求する試験を行う。ネットワーク観測で映像送信は0、提案中止後も既存の字幕をオフラインで編集できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/transcript_tests.rs](../../../../crates/engine/src/transcript_tests.rs)。
- 対応を確認したテスト：[generate_without_a_transcriber](../../../../crates/engine/src/transcript_tests.rs)。
