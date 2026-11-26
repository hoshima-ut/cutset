# レイアウト追従の作業・試験（GR-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-GR-03`、受入IDは `AC-GR-03`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

左右余白12pxの帯、入場10・退場5の50フレーム配置を100へ伸ばす。文字変更後も余白12px、入退場は10と5のままになる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [pins_follow_text_growth](../../../../crates/engine/src/graphic_templates/tests.rs#L252) は <code>graphics.pin</code> を呼ぶ。
- [responsive_time_protects_intro_and_outro_when_trimmed](../../../../crates/engine/src/graphic_templates/tests.rs#L173) は <code>graphics.setResponsiveTime</code> を呼ぶ。
- [rolls_at_exact_times](../../../../crates/engine/src/graphic_templates/tests.rs#L226) は <code>graphics.setRoll</code> を呼ぶ。
- 対応を確認したテスト：[pins_follow_text_growth](../../../../crates/engine/src/graphic_templates/tests.rs)。
