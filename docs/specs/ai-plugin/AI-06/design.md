# AI-06 拡張のコマンド契約 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

プラグインが利用可能な操作、対象、パラメーターを照会し、編集案を提出する。UIは対象・差分・制限を表示し、利用者の確定操作を共有する。

## データと処理境界

既存コマンドのID・引数・有効状態を参照し、提案用の許可リストに写像する。外部公開は検査・提案・適用の権限を分け、整合性検査をエンジンへ集約する。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[crates/automation/src/server.rs](../../../../crates/automation/src/server.rs)。

確認した関数：[command_list](../../../../crates/automation/src/server.rs)。既存のMCPがcommand.listを呼び、操作の列挙と絞り込みを提供する。公式AIに渡す能力の許可リスト、提案専用権限、エンジンへの確定委譲は別途設計する。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>command.list</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>state.inspect</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
