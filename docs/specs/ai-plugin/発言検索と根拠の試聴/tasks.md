# 発言検索と根拠の試聴の作業・試験（AI-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AI-02`、受入IDは `AC-AI-02`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

二人の「こうしょう」が別々の時刻にある素材を用意する。双方の候補から対応する音声を試聴でき、一方の表記を変えてもカット数と映像尺は変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/transcript_tests.rs](../../../../crates/engine/src/transcript_tests.rs)。
- 対応を確認したテスト：[generate_inspect_search_and_rename](../../../../crates/engine/src/transcript_tests.rs)。
