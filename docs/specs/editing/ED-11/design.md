# ED-11 トラック管理 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

トラックを追加・命名し、表示、ミュート、ソロ、ロックを独立に切り替える。ヘッダーの高さを調整する。

## データと処理境界

トラックIDと並び番号を区別する。視聴に影響する出力状態、編集権限、単なる表示寸法を別項目として保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.addTracks</code> | <code>{"video":n=1,"audio":n=0,"submix":n=0,"videoAfter":"first"&#124;"V2"&#124;n?,"audioAfter":"first"&#124;"A2"&#124;n?,"submixAfter":"first"&#124;"S1"&#124;n?,"audioType":"standard&#124;5.1&#124;adaptive&#124;mono"?,"submixType":"stereo&#124;5.1&#124;adaptive&#124;mono"?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.deleteTrack</code> | <code>{"track":"V3"&#124;id}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.deleteTracks</code> | <code>{"video":"empty"&#124;"V2"&#124;id?,"audio":"empty"&#124;"A2"&#124;id?,"captions":"empty"&#124;"C2"&#124;id?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>timeline.moveAudioTargetsDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.moveAudioTargetsUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.moveVideoTargetsDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.moveVideoTargetsUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.setTargeting</code> | <code>{"track":"V1"&#124;id,"targeted":bool?,"sourcePatch":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.setTrack</code> | <code>{"track":"V1"&#124;id,"locked":bool?,"syncLock":bool?,"enabled":bool?,"muted":bool?,"solo":bool?,"name":str?,"volumeDb":f64?,"pan":f64?,"label":"Violet&#124;Iris&#124;…"&#124;""&#124;null?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.toggleAllAudioTargets</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleAllVideoTargets</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleMuteTargetedAudio</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleOutputTargetedVideo</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleSoloTargetedAudio</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA1</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA2</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA3</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA4</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA6</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA7</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetA8</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV1</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV2</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV3</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV4</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV6</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV7</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleTargetV8</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
