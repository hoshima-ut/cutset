# 案件の取り込みポリシーの作業・試験（MN-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-MN-02`、受入IDは `AC-MN-02`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

参照で素材Aを登録後、複製へ変更してBを登録する。Aは旧パス、Bはコピー先を指し、案件再開後もその対応が保たれる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[crates/engine/src/proxies_tests.rs](../../../../crates/engine/src/proxies_tests.rs)。
- 対応を確認したテスト：[ingest_copies_and_creates_proxies_on_import](../../../../crates/engine/src/proxies_tests.rs)。
