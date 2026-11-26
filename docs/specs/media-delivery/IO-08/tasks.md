# IO-08 レイヤー画像 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-08`、受入IDは `AC-IO-08`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

200×100の画像の右半分だけに半透明の前景を置く。個別読み込みは2層を返し、上下を重ねると統合画像と同位置・同じ透過結果になる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/media/src/still/psd/tests.rs](../../../../crates/media/src/still/psd/tests.rs)。
- 対応を確認したテスト：[merged_alpha_only_when_the_layer_count_says_so](../../../../crates/media/src/still/psd/tests.rs)。
