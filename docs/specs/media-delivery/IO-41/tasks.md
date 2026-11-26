# IO-41 出力プリセット — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-41`、受入IDは `AC-IO-41`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

1920×1080の設定で登録後、プリセットを1280×720に変更して2本目を登録する。各ジョブが登録時の寸法で出力される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [quick_export_uses_and_remembers_a_preset](../../../../crates/engine/src/export_tests.rs#L936) は <code>export.quick</code> を呼ぶ。
- [ranges_resolve_and_sidecar_captions_are_written](../../../../crates/engine/src/export_tests.rs#L954) は <code>export.resolve</code> を呼ぶ。
- [user_presets_persist_with_favourites_import_and_export](../../../../crates/engine/src/export_tests.rs#L623) は <code>export.presets.export</code> を呼ぶ。
