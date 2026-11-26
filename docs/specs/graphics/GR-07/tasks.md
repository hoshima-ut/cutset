# GR-07 タイトルテンプレート — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-GR-07`、受入IDは `AC-GR-07`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

文字列だけ公開したテンプレートを2回配置する。Aに「主将」、Bに「監督」を設定し、再読込でそれぞれの本文が残り、内部図形の非公開値は変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [builtin_templates_apply_and_thumbnail](../../../../crates/engine/src/graphic_templates/tests.rs#L147) は <code>graphics.template.apply</code> を呼ぶ。
- [remove_picks_one_library_file_and_never_a_path_outside_it](../../../../crates/engine/src/graphic_templates/tests.rs#L711) は <code>graphics.template.remove</code> を呼ぶ。
- [template_export_install_apply_round_trip](../../../../crates/engine/src/graphic_templates/tests.rs#L63) は <code>graphics.template.apply</code> を呼ぶ。
