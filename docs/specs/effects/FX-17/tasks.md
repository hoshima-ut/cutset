# FX-17 ジャンプカットの補間 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-17`、受入IDは `AC-FX-17`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25fpsの正面顔で中央揃え8フレームを設定する。補間区間外のフレームと音声は元に一致し、解除すると区間内も通常の編集点に戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/render/src/flow.rs](../../../../crates/render/src/flow.rs)。
- 対応を確認したテスト：[morph_cut_moves_the_subject_instead_of_double_exposing](../../../../crates/render/src/transitions/tests.rs)。
