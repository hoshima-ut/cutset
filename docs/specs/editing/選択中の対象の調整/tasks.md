# 選択中の対象の調整の作業・試験（ED-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-07`、受入IDは `AC-ED-07`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ素材の配置A/B/CのうちA/Bの音量を−6 dBにする。Cと原本は維持し、Undo一回でA/Bの異なる旧値が戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/ui-egui/src/panels/effect_controls.rs](../../../../crates/ui-egui/src/panels/effect_controls.rs)。
