# ED-29 スリップ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

配置を選択し、前後の境界フレームを表示しながら参照素材だけを前後させる。

## データと処理境界

配置の開始・尺を固定し、素材In/Outを同じ量だけずらす。リンク対象は全員に共通する許容差分で更新する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/slip.rs](../../../../crates/engine/src/slip.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>timeline.slip</code> | <code>{"clip":id,"delta":ticks&#124;"deltaFrames":i64}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.slipLeft</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.slipLeft5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.slipPreview</code> | <code>{"clip":id,"delta":ticks&#124;"deltaFrames":i64}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.slipRight</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.slipRight5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
