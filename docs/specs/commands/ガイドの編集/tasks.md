# ガイドの編集の作業・試験（MN-23）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-MN-23`、受入IDは `AC-MN-23`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

1920幅の画面の50%に縦線を追加する。2倍ズーム後も映像座標960にあり、書き出した静止画に線が含まれない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/ui-egui/src/panels/monitor_view.rs](../../../../crates/ui-egui/src/panels/monitor_view.rs)。
- 対応を確認したテスト：[magnification_pans_and_guides_from_rulers](../../../../crates/ui-egui/tests/it/view_ui.rs)。
