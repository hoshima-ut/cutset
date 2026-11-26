# 生成素材の来歴の作業・試験（AI-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AI-08`、受入IDは `AC-AI-08`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

元配置の後ろへ12フレームを生成挿入し、接続を解除して再生・書き出す。再推論要求が0で12フレームが再現し、削除後は元配置の終了位置と素材参照が一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/narration_tests.rs](../../../../crates/engine/src/narration_tests.rs)。
- 対応を確認したテスト：[create_places_the_narration_at_the_playhead_as_one_undo_step](../../../../crates/engine/src/narration_tests.rs)。
