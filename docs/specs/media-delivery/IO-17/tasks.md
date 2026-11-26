# IO-17 ラベル・時刻・注記 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-17`、受入IDは `AC-IO-17`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ素材を2回配置し素材マーカーを1件、シーケンスマーカーを1件付ける。前者だけが両方の使用箇所に対応し、DF分境界を往復しても位置が動かない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [close_project_and_save_all](../../../../crates/engine/src/clip_ops_tests.rs#L330) は <code>edit.label.tan</code> を呼ぶ。
- [label_commands_and_select_label_group](../../../../crates/engine/src/clip_ops_tests.rs#L93) は <code>edit.selectLabelGroup</code> を呼ぶ。
- [label_presets_import_export_and_delete](../../../../crates/engine/src/settings_tests.rs#L1067) は <code>labels.presets</code> を呼ぶ。
