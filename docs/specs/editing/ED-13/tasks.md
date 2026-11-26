# ED-13 ロックと連動 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-13`、受入IDは `AC-ED-13`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

10フレーム挿入し、同期対象の字幕が100→110、同期を外した字幕とロック済みBGMが100のままであることを比較する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/locked_clip_edits_tests.rs](../../../../crates/engine/src/locked_clip_edits_tests.rs)。
- 対応を確認したテスト：[ripple_delete_shifts_sync_locked_caption_tracks_and_restores_on_undo](../../../../crates/engine/src/ripple_delete_tests.rs)。
