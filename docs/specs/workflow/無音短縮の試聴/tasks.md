# 無音短縮の試聴の作業・試験（UX-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UX-06`、受入IDは `AC-UX-06`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25fps、1600フレームの案件でA40・B60を採用しC25を残す。新しい終端1500とC[700,725)を照合し、字幕修正だけでは再び短くならない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/transcript_tests.rs](../../../../crates/engine/src/transcript_tests.rs)。
- 関連する既存テストモジュール：[crates/edit/src/transcript/tests.rs](../../../../crates/edit/src/transcript/tests.rs)。
- 対応を確認したテスト：[pauses_are_found_and_removed_in_one_pass](../../../../crates/edit/src/transcript/tests.rs)。
