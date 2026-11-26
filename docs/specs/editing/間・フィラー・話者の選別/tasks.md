# 間・フィラー・話者の選別の作業・試験（ED-43）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-43`、受入IDは `AC-ED-43`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

間が[20,30)と[50,70)にあるとき後者だけを採用する。終端が20フレーム減り、[20,30)の内容と長さは元のまま。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [remove_fillers_pauses_and_create_captions](../../../../crates/engine/src/transcript_tests.rs#L108) は <code>transcript.removePauses</code> を呼ぶ。
