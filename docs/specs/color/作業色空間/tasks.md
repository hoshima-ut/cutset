# 作業色空間の作業・試験（CO-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CO-02`、受入IDは `AC-CO-02`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

線形の0.18・0.5・1.0のパッチを既知の変換で往復する。同一変換を一度だけ適用した参照値と照合し、設定を元に戻すと最初の値に戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [export_cube_exports_an_apply_match_result_and_refuses_what_it_cannot](../../../../crates/engine/src/color_tests.rs#L380) は <code>sequence.colorSettings</code> を呼ぶ。
- [hdr_lumetri_and_mastering_metadata_through_commands](../../../../crates/engine/src/color_tests.rs#L230) は <code>sequence.colorSettings</code> を呼ぶ。
- [interpret_footage_and_sequence_colour_settings](../../../../crates/engine/src/color_tests.rs#L163) は <code>sequence.colorSettings</code> を呼ぶ。
