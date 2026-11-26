# 文字起こしから字幕の作業・試験（CC-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CC-01`、受入IDは `AC-CC-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25fpsの配置で発話が[25,50)・[75,100)にある。別話者の2発話を字幕化し、後者の名前を直しても最初の字幕と映像尺、元発話の時刻が変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [remove_fillers_pauses_and_create_captions](../../../../crates/engine/src/transcript_tests.rs#L108) は <code>transcript.createCaptions</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/captions/tests.rs](../../../../crates/engine/src/captions/tests.rs)。
