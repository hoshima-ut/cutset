# UI-17 欠落素材と音の診断 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-17`、受入IDは `AC-UI-17`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

音声素材を移動した案件で再リンク前後を比較する。オフライン時も配置の時刻と字幕を保持し、復帰後に同じ位置のテスト音が鳴る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [events_log_failed_commands_jobs_and_messages](../../../../crates/engine/src/panels_tests.rs#L124) は <code>events.clear</code> を呼ぶ。
- [events_report_background_jobs](../../../../crates/engine/src/panels_tests.rs#L155) は <code>events.clear</code> を呼ぶ。
- [events_show_a_finished_exports_warnings](../../../../crates/engine/src/panels_tests.rs#L182) は <code>events.clear</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/relink_tests.rs](../../../../crates/engine/src/relink_tests.rs)。
