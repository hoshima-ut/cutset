# モデルとエージェントの接続の設計（AI-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

設定で接続方式とモデルを選び、対応入力・処理先・請求元を確認する。外部エージェントでは本人の公式クライアントから制限付き提案ツールを呼ぶ。

## データと処理境界

モデルアダプターは能力、提案ストリーム、取消、認証・利用枠エラーを返す。資格情報はホストの保管領域へ置き、プラグインには接続IDと許可済み能力だけを渡す。

## 既存実装との対応

方針は「新規設計」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[apps/filmcraft/src/control_server.rs](../../../../apps/filmcraft/src/control_server.rs)。

確認した関数：[serve_lines](../../../../apps/filmcraft/src/control_server.rs)。デスクトップの制御プロトコルには要求トークンと一行のサイズ上限を渡す認証境界がある。これはローカル制御用で、モデル提供者のOAuth・APIキー保管・課金権限・プラグインの隔離は別途実装する。

詳細は[個別の設計書](../../../architecture/model-connections.md)を参照する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
