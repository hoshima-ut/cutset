# FX-12 被写体の追跡 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-12`、受入IDは `AC-FX-12`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

白い円が1フレーム2画素動き10〜14で遮蔽される素材を使う。遮蔽後の15にアンカーを置き直しても0〜9の輪郭と15の手指定位置は変化しない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/masks_tests.rs](../../../../crates/engine/src/masks_tests.rs)。
- 対応を確認したテスト：[tracking_follows_known_motion_forward_and_backward](../../../../crates/engine/src/masks_tests.rs)。
