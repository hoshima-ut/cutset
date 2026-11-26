# ED-55 マーカーの所属と範囲 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材モニターと完成モニターでそれぞれマーカーを付け、所属、開始、長さ、コメントを指定して検索する。

## データと処理境界

素材マーカーは原本IDと元時刻、シーケンスマーカーはシーケンスIDと時刻を持つ。使用箇所へ投影する際は配置の素材点と速度を使う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/marker_edit.rs](../../../../crates/engine/src/marker_edit.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>markers.add</code> | <code>{"target":"program&#124;source","time":ticks?,"name":str?,"comment":str?,"color":label_or_hex?,"author":str?,"durationFrames":i64?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.addChapter</code> | <code>{"time":ticks?,"name":str?,"comment":str?,"color":label_or_hex?,"author":str?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.addFlashCue</code> | <code>{"time":ticks?,"name":str?,"comment":str?,"color":label_or_hex?,"author":str?}</code> | [sequence_extras.rs](../../../../crates/engine/src/sequence_extras.rs) |
| <code>markers.addRange</code> | <code>{"time":ticks?,"durationFrames":i64=1s,"duration":ticks?,"name":str?,"comment":str?,"color":label_or_hex?,"author":str?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.addRangeInOut</code> | <code>{"name":str?,"comment":str?,"color":label_or_hex?,"author":str?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.clearAll</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.clearCurrent</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.clearIn</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.clearInOut</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.clearOut</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.copyPasteIncludesSequenceMarkers</code> | <code>{"on":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.delete</code> | <code>{"target":"program&#124;source","sequence":id?,"item":id?,"marker":id&#124;"markers":[id]}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.edit</code> | <code>{"target":"program&#124;source","sequence":id?,"item":id?,"marker":id&#124;"markers":[id],"time":ticks?,"frame":i64?,"durationFrames":i64?,"name":str?,"comment":str?,"author":str?,"url":str?,"color":label_or_hex?,"kind":"comment&#124;chapter&#124;segmentation&#124;webLink&#124;flashCue"?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.exportCsv</code> | <code>{"path":str} (all markers in the active sequence)</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.filterColors</code> | <code>{"hidden":[label_or_hex]}&#124;{"color":label_or_hex,"visible":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.goNext</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.goPrev</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.goToIn</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.goToOut</code> | <code>{"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.goToSplitAudioIn</code> | <code>{"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.goToSplitAudioOut</code> | <code>{"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.goToSplitVideoIn</code> | <code>{"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.goToSplitVideoOut</code> | <code>{"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.markClip</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.markIn</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.markOut</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program&#124;source"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.markSelection</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>markers.markSplitAudioIn</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.markSplitAudioOut</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.markSplitVideoIn</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.markSplitVideoOut</code> | <code>{"time":ticks?,"frame":i64?,"seconds":f64?,"timecode":str?,"target":"program&#124;source"}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.rippleSequenceMarkers</code> | <code>{"on":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>markers.showAllMarkerColors</code> | <code>{}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
