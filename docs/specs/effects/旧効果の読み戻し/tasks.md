# 旧効果の読み戻しの作業・試験（FX-18）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-18`、受入IDは `AC-FX-18`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

未知IDの効果に独自値7と2個のキーを含めて保存再開する。保存後もID・値・時刻が一致し、該当配置をバイパスして再生できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [builtins_apply_and_user_presets_persist](../../../../crates/engine/src/presets_tests.rs#L163) は <code>presets.apply</code> を呼ぶ。
- [export_and_import_go_through_host_services](../../../../crates/engine/src/presets_tests.rs#L245) は <code>presets.export</code> を呼ぶ。
- [import_collision_picks_suffixed_filename](../../../../crates/engine/src/presets_tests.rs#L434) は <code>presets.import</code> を呼ぶ。
