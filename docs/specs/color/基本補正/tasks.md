# 基本補正の作業・試験（CO-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CO-04`、受入IDは `AC-CO-04`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

色票に対して彩度を0にして、有彩色が無彩色になることを確認する。自動補正の後に露光だけを変え、他の自動設定値が保持される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [apply_match_grades_the_clip_towards_the_reference](../../../../crates/engine/src/color_tests.rs#L135) は <code>lumetri.applyMatch</code> を呼ぶ。
- [export_cube_exports_an_apply_match_result_and_refuses_what_it_cannot](../../../../crates/engine/src/color_tests.rs#L380) は <code>lumetri.applyMatch</code> を呼ぶ。
- [export_cube_gives_the_render_when_applied_to_the_ungraded_frame](../../../../crates/engine/src/color_tests.rs#L332) は <code>lumetri.exportCube</code> を呼ぶ。
