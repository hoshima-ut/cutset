# GR-02 図形・画像レイヤー — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-GR-02`、受入IDは `AC-GR-02`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

帯を(10,20)、ロゴを(30,25)に置き、同じグループを右へ12移す。結果は(22,20)と(42,25)で、前後を入れ替えると重なる画素だけ変化する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [arrange_select_and_reset](../../../../crates/engine/src/graphics/tests.rs#L466) は <code>graphics.set</code> を呼ぶ。
- [linear_gradient_fill_sets_and_evaluates](../../../../crates/engine/src/graphics/tests.rs#L286) は <code>graphics.set</code> を呼ぶ。
- [select_next_graphic_and_reset_duration](../../../../crates/engine/src/graphics/tests.rs#L508) は <code>graphics.resetDuration</code> を呼ぶ。
