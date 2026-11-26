# AI-09 モデルとエージェントの接続 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AI-09`、受入IDは `AC-AI-09`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

ローカル・BYOK・対象プラン・外部ホストの模擬接続へ同じ字幕区間を入力する。同じ構造の案が得られ、1経路を失効させても他経路への自動送信と案件ファイル内の鍵は0件となる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 関連する既存テストモジュール：[apps/filmcraft/src/control_server/tests.rs](../../../../apps/filmcraft/src/control_server/tests.rs)。
- 対応を確認したテスト：[authentication_is_required_on_every_request](../../../../apps/filmcraft/src/control_server/tests.rs)。
