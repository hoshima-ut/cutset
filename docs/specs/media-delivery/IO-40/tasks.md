# IO-40 納品範囲 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-40`、受入IDは `AC-IO-40`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25 fpsでフレーム番号を焼いた素材から内部範囲[10,11)と[10,20)を出す。前者は10だけ、後者は10〜19の10枚になる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [export_selection_project_and_ale](../../../../crates/engine/src/project_tools/tests.rs#L190) は <code>file.exportSelectionProject</code> を呼ぶ。
- [export_selection_project_of_a_bin_exports_its_contents](../../../../crates/engine/src/project_tools/tests.rs#L224) は <code>file.exportSelectionProject</code> を呼ぶ。
- [export_interchange_refuses_an_unknown_format](../../../../crates/engine/src/tests.rs#L1019) は <code>file.exportInterchange</code> を呼ぶ。
