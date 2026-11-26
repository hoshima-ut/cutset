# 書き出し状況の作業・試験（UI-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-12`、受入IDは `AC-UI-12`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

版Aの50フレームを書き出し中に版Bを60フレームへ編集する。完了したジョブは版Aの50フレームを報告し、次のジョブから版Bを選択できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [tracking_runs_in_the_background_and_can_be_cancelled](../../../../crates/engine/src/masks_tests.rs#L298) は <code>jobs.cancel</code> を呼ぶ。
- [jobs_list_reports_an_exports_offline_media](../../../../crates/engine/src/relink_tests.rs#L321) は <code>jobs.list</code> を呼ぶ。
- [background_job_reports_progress_and_cancel_changes_nothing](../../../../crates/engine/src/scene_detect/tests.rs#L118) は <code>jobs.cancel</code> を呼ぶ。
