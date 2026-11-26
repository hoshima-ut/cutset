# ED-41 素材・完成版の文字起こし — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-41`、受入IDは `AC-ED-41`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

左右に異なる文を入れた音声で右を指定し、認識行が右の文と右の発話時刻を指すか照合する。シーケンスの先頭を切った後も元音に戻れる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [generate_inspect_search_and_rename](../../../../crates/engine/src/transcript_tests.rs#L43) は <code>transcript.generate</code> を呼ぶ。
- [generate_without_a_transcriber](../../../../crates/engine/src/transcript_tests.rs#L162) は <code>transcript.generate</code> を呼ぶ。
- [remove_fillers_pauses_and_create_captions](../../../../crates/engine/src/transcript_tests.rs#L108) は <code>transcript.removeFillers</code> を呼ぶ。
