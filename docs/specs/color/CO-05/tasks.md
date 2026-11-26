# CO-05 ルックとLUT — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CO-05`、受入IDは `AC-CO-05`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

恒等LUTと赤青を入れ替えるLUTを赤パッチに適用する。恒等は赤、後者の強度0は赤、100%は青となり、別端末でも同じLUTの内容を確認できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [export_builtin_and_library_luts](../../../../crates/engine/src/color_tests.rs#L94) は <code>lut.export</code> を呼ぶ。
- [import_lut_set_input_and_look_then_undo](../../../../crates/engine/src/color_tests.rs#L51) は <code>lut.import</code> を呼ぶ。
