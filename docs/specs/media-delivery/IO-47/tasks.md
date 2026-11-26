# IO-47 フレームと連番出力 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-47`、受入IDは `AC-IO-47`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

[98,101)を開始番号7・3桁で出す。007〜009が生成され、順に元フレーム98〜100を示し、透明な画素のアルファを保持する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [a_frame_still_loading_is_reported_not_saved_blank](../../../../crates/engine/src/frame_export_tests.rs#L123) は <code>file.exportFrame</code> を呼ぶ。
- [an_earlier_deferred_read_does_not_fail_the_export](../../../../crates/engine/src/frame_export_tests.rs#L147) は <code>file.exportFrame</code> を呼ぶ。
- [frame_export_selects_the_correct_monitor_time_and_original_media](../../../../crates/engine/src/frame_export_tests.rs#L25) は <code>file.exportFrame</code> を呼ぶ。
