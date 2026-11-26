# 画面上の文字組みの作業・試験（GR-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-GR-01`、受入IDは `AC-GR-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

幅を狭くした段落枠で「東京ABC」を入力し、未確定中に矢印で候補を選ぶ。タイムラインは動かず、確定文字と改行が保存再開した画面と書き出しで揃う。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [new_text_makes_a_graphic_clip_above_the_footage](../../../../crates/engine/src/graphics/tests.rs#L124) は <code>graphics.newText</code> を呼ぶ。
- [a_layer_saved_before_the_box_height_existed_can_still_get_one](../../../../crates/engine/src/graphics/tests.rs#L715) は <code>graphics.newText</code> を呼ぶ。
- [a_property_drag_is_one_undo_step](../../../../crates/engine/src/graphics/tests.rs#L185) は <code>graphics.newText</code> を呼ぶ。
