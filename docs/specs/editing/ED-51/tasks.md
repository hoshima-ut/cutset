# ED-51 受け渡し用の展開 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-51`、受入IDは `AC-ED-51`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

マルチカム切替1件を単一カメラに展開する。コピーの切替後の素材点を3フレーム延長でき、元シーケンスは角度変更が引き続き可能。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [simplify_sequence_makes_a_clean_copy](../../../../crates/engine/src/sequence_extras/tests.rs#L167) は <code>sequence.simplify</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/nest_fidelity_tests.rs](../../../../crates/engine/src/nest_fidelity_tests.rs)。
