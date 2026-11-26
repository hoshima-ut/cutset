# ED-10 タイムライン移動 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

シーケンスタブを選び、時刻入力、前後の編集点、配置の検索結果から移動する。ズームは現在位置を基準にする。

## データと処理境界

案件IDとシーケンスIDを移動のキーとし、再生ヘッド、ズームと選択を各タブで保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/timeline.rs](../../../../crates/ui-egui/src/panels/timeline.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.close</code> | <code>{"item":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.closeOthers</code> | <code>{"item":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.duplicateFrames</code> | <code>{}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.goToNextGap</code> | <code>{}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.goToNextGapInTrack</code> | <code>{"track":"V1"&#124;id?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.goToPrevGap</code> | <code>{}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.goToPrevGapInTrack</code> | <code>{"track":"V1"&#124;id?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.inspect</code> | <code>{"item":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.linkedSelection</code> | <code>{"on":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.moveTab</code> | <code>{"item":id?,"index":int}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.normalizeMixTrack</code> | <code>{"db":f64=0}</code> | [sequence_extras.rs](../../../../crates/engine/src/sequence_extras.rs) |
| <code>sequence.open</code> | <code>{"item":id}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.revealInProject</code> | <code>{"item":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.selectionFollowsPlayhead</code> | <code>{"on":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.setWorkArea</code> | <code>{"start":ticks,"end":ticks}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.setWorkAreaIn</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.setWorkAreaOut</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.settings</code> | <code>{"width":u32?,"height":u32?,"fps":f64?,"name":str?,"sampleRate":u32?,"mix":"Stereo&#124;Mono&#124;5.1&#124;Adaptive"?,"dropFrame":bool?,"videoDisplay":"timecode&#124;feet35&#124;feet16&#124;frames"?,"maxRenderQuality":bool?,"workingSpace":"rec709"&#124;"rec2100-pq"&#124;"rec2100-hlg"?,"wideGamut":bool?,"autoToneMap":bool?,"scaleMotion":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.showDuplicateFrameMarkers</code> | <code>{"on":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.showThroughEdits</code> | <code>{"on":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.snap</code> | <code>{"on":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.throughEdits</code> | <code>{}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.workAreaBar</code> | <code>{"show":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.move</code> | <code>{"moves":[{"clip":id,"track":id&#124;"V2"&#124;"new" (after the last of its kind),"time":ticks&#124;{"seconds":f}&#124;{"frame":n}&#124;{"timecode":str}}],"insert":bool,"linked":bool?,"copy":bool?,"captions":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.nudgeDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.nudgeLeft</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.nudgeLeft5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.nudgeRight</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.nudgeRight5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.nudgeUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.place</code> | <code>{"item":id&#124;"items":[id] (back to back, one undo step),"track":"V1"&#124;id&#124;"A1" (sound only)&#124;"new" (a video track after the last)?,"audioTrack":"A1"&#124;id&#124;"new"?,"time":ticks&#124;"frame":i64&#124;"seconds":f64,"insert":bool,"sourceIn":ticks&#124;{"frame"&#124;"seconds"&#124;"timecode"}?,"duration":ticks&#124;{"frame"&#124;"seconds"&#124;"timecode"}?,"video":bool=true,"audio":bool=true,"matchSequence":bool=false (an empty sequence first takes the clip's frame size and rate)}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.toggleAllSourceAudio</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.toggleAllSourceVideo</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
