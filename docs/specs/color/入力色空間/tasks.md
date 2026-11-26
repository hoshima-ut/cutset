# 入力色空間の作業・試験（CO-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CO-01`、受入IDは `AC-CO-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ色票を一方は正しく、一方は誤ったタグで取り込む。後者の解釈だけを修正し、同じ作業空間で中立パッチのRGB値が参照値と一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [color_info_says_which_values_no_tag_gave](../../../../crates/engine/src/color_tests.rs#L292) は <code>media.colorInfo</code> を呼ぶ。
- [hdr_lumetri_and_mastering_metadata_through_commands](../../../../crates/engine/src/color_tests.rs#L230) は <code>media.colorInfo</code> を呼ぶ。
- [interpret_footage_and_sequence_colour_settings](../../../../crates/engine/src/color_tests.rs#L163) は <code>color.spaces</code> を呼ぶ。
