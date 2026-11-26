# 字幕のグラフィック化の作業・試験（MN-20）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-MN-20`、受入IDは `AC-MN-20`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

日本語3キューの中央1件を変換する。サイドカーに残るのは2件、中央の本文は元と同じ時間に映像として描画され、Undoで3キューに戻る。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/graphic_templates/tests.rs](../../../../crates/engine/src/graphic_templates/tests.rs)。
- 対応を確認したテスト：[upgrade_caption_to_graphic](../../../../crates/engine/src/graphic_templates/tests.rs)。
