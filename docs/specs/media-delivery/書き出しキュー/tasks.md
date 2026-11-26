# 書き出しキューの作業・試験（IO-48）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-48`、受入IDは `AC-IO-48`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

横版と縦版を別パスで登録し、横版だけを中止する。縦版は完了し、横版の再試行で指定尺の完成品が1件できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [queue_cancels_a_running_export_and_retries_a_failed_one](../../../../crates/engine/src/export_tests.rs#L738) は <code>export.queue.cancel</code> を呼ぶ。
- [queue_move_by_extreme_offsets_clamps_instead_of_overflowing](../../../../crates/engine/src/export_tests.rs#L722) は <code>export.queue.move</code> を呼ぶ。
- [queue_orders_cancels_and_retries](../../../../crates/engine/src/export_tests.rs#L680) は <code>export.queue.cancel</code> を呼ぶ。
