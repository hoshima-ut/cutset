# ヘッド追従と連続境界の作業・試験（MN-15）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-MN-15`、受入IDは `AC-MN-15`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同素材の[0,10)と[10,20)、別素材を順に並べる。連続表示は最初の境界だけに現れ、切替前後で書き出しの尺は変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/edit/src/through.rs](../../../../crates/edit/src/through.rs)。
- 対応を確認したテスト：[selection_follows_playhead](../../../../crates/engine/src/sequence_tools_tests.rs)。
