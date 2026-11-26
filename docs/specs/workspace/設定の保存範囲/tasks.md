# 設定の保存範囲の作業・試験（UI-14）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-UI-14`、受入IDは `AC-UI-14`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

案件Aのシーケンスだけ表示形式を変え、端末の外観設定も変更する。案件Bで外観の変更だけが見え、再起動後も範囲が同じになる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [favorite_themes_validate_and_persist_without_changing_other_settings](../../../../crates/engine/src/settings_tests.rs#L998) は <code>prefs.set</code> を呼ぶ。
- [graphics_text_uses_the_text_settings](../../../../crates/engine/src/settings_tests.rs#L576) は <code>prefs.set</code> を呼ぶ。
- [hardware_decoding_setting_drives_the_decoder_switch](../../../../crates/engine/src/settings_tests.rs#L874) は <code>prefs.set</code> を呼ぶ。
