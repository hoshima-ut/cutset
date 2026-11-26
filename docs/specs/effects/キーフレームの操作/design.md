# キーフレームの操作の設計（FX-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

再生ヘッドでアニメーションを有効にしてキーを加える。キーの一覧から対象だけを選び、1フレーム移動・削除した結果をモニターで確認する。

## データと処理境界

効果インスタンス、プロパティ、ローカル時刻で編集対象を特定する。キー移動時は値と補間設定を保持し、値型に応じた精度で保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/keyframe_move.rs](../../../../crates/engine/src/keyframe_move.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>effects.addKeyframe</code> | <code>{"clip":id,"effect":str&#124;index,"param":str,"mask":n?,"time":ticks?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.deleteKeyframe</code> | <code>{"clip":id,"effect":str&#124;index,"param":str,"mediaTime":ticks}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.moveKeyframe</code> | <code>{"clip":id,"effect":str&#124;index,"param":str,"mediaTime":ticks,"to":ticks,"value":any?,"merge":bool?,"begin":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.moveKeyframes</code> | <code>{"keyframes":[{"clip":id,"effect":index,"param":str,"mask":n?,"time":mediaTicks}],"delta":timelineTicks}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.setKeyframe</code> | <code>{"clip":id,"effect":str&#124;index,"param":str,"mediaTime":ticks,"value":any?,"inInfluence":0..1?,"outInfluence":0..1?,"merge":bool?,"begin":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
