# GR-05 再利用するスタイル — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-GR-05`、受入IDは `AC-GR-05`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ白文字スタイルの2枚のうちBだけ赤にする。共有のサイズを36から48へ変えると両方48で、Bの赤と別スタイル字幕のサイズは変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [align_and_distribute_layers](../../../../crates/engine/src/graphics/tests.rs#L260) は <code>graphics.align</code> を呼ぶ。
- [align_puts_a_pinned_layer_where_it_asks](../../../../crates/engine/src/graphics/tests.rs#L902) は <code>graphics.align</code> を呼ぶ。
- [align_menu_commands_frame_group_and_selection](../../../../crates/engine/src/graphics/tests.rs#L401) は <code>graphics.alignFrame.left</code> を呼ぶ。
