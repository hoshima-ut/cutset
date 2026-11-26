# 映像スコープの作業・試験（CO-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CO-09`、受入IDは `AC-CO-09`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

黒、50%灰、白を同面積にした既知信号を入力する。同一レンジでヒストグラムに3群、波形に3段が現れ、灰色のRGBパレードは3成分が揃う。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [scopes_read_finds_the_colour_bar_targets](../../../../crates/engine/src/scopes_tests.rs#L51) は <code>scopes.read</code> を呼ぶ。
- [scopes_read_reports_exact_levels_of_a_colour_matte](../../../../crates/engine/src/scopes_tests.rs#L16) は <code>scopes.read</code> を呼ぶ。
