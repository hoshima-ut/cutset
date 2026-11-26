# UI-16 実行環境の診断 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-16`、受入IDは `AC-UI-16`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

入力を読めるが目的のエンコーダーがない環境で診断し、再生可・指定形式出力不可を別々に確認する。既存出力の内容は変化しない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [system_report_lists_the_build](../../../../crates/engine/src/project_tools/tests.rs#L557) は <code>help.systemReport</code> を呼ぶ。
- [perf_stats_query_reports_decode_counters](../../../../crates/engine/src/perf.rs#L84) は <code>perf.stats</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/menu_dialogs.rs](../../../../crates/ui-egui/src/panels/menu_dialogs.rs)。
- 対応を確認したテスト：[system_report_lists_the_build](../../../../crates/engine/src/project_tools/tests.rs)。
