# UI-06 二つのモニター — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-06`、受入IDは `AC-UI-06`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25fpsで素材側を50、完成側を125フレームに置く。素材側で1フレーム進めてInを設定すると素材Inが51になり、完成側は125のままになる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。
- 対応を確認したテスト：[space_targets_the_focused_monitor_and_output_is_exclusive](../../../../crates/ui-egui/tests/it/source_playback_ui.rs)。
