# ED-32 トリムの試聴 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

トリムモードで編集点の前後をループし、1フレームまたは指定ステップで動かしてから確定または取消する。

## データと処理境界

選択した編集点、対象トラック、トリム種別、前後の試聴長をセッションに保持する。連続操作を確定単位へまとめる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/trim_monitor.rs](../../../../crates/ui-egui/src/panels/trim_monitor.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>trim.applyDefaultTransition</code> | <code>{"clips":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.backward</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.backwardMany</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.cancelDynamic</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.clear</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.edit</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.extendNextEdit</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>trim.extendPreviousEdit</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>trim.extendToPlayhead</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.forward</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.forwardMany</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.monitor</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.next</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.nudge</code> | <code>{"frames":i64}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.playAround</code> | <code>{"clock":seconds,"loop":bool=true,"toggle":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.previous</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.rippleNext</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.ripplePrevious</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.selectEditPoint</code> | <code>{"clip":id,"edge":"in&#124;out","kind":"trim&#124;ripple&#124;roll","add":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.selectNearest</code> | <code>{"kind":"rippleIn&#124;rippleOut&#124;roll&#124;trimIn&#124;trimOut"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.shuttle</code> | <code>{"direction":"forward&#124;reverse","slow":bool?,"clock":seconds}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.shuttleStop</code> | <code>{"clock":seconds?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.tick</code> | <code>{"clock":seconds}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>trim.toggleType</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
