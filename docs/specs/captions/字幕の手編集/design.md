# 字幕の手編集の設計（CC-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

字幕を選び、再生ヘッドの分割位置と本文の分割箇所を指定する。隣接字幕の結合や端のトリムはタイムラインと一覧に同時反映する。

## データと処理境界

開始を含み終了を含まない区間を正確な時間単位で保持し、同一トラックの字幕は重複させない。本文の改行・話者・トラックスタイルを引き継ぐ。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/graphics/ime.rs](../../../../crates/ui-egui/src/panels/graphics/ime.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>captions.add</code> | <code>{"track":id&#124;"C1"?,"text":str?,"time":ticks?,"seconds":f64?,"durationSeconds":f64=3}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.delete</code> | <code>{"captions":[id]?,"ripple":bool=false}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.deleteTrack</code> | <code>{"track":id&#124;"C1"}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.duplicate</code> | <code>{"captions":[id]?,"delta":ticks&#124;"deltaFrames":i64}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.goTo</code> | <code>{"caption":id}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.hideAll</code> | <code>{}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.list</code> | <code>{"track":id&#124;"C1"?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.merge</code> | <code>{"captions":[id]?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.move</code> | <code>{"captions":[id]?,"delta":ticks&#124;"deltaFrames":i64}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.newTrack</code> | <code>{"format":"Subtitle&#124;CEA-608&#124;CEA-708&#124;Teletext","name":str?,"language":str?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.next</code> | <code>{}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.previous</code> | <code>{}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.select</code> | <code>{"captions":[id],"add":bool?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.setStyle</code> | <code>{"track":id&#124;"C1","font":str?,"fontStyle":str="SemiBold" (Regular, Medium, Bold…)?,"size":f32?,"color":"#rrggbb[aa]"?,"background":bool?,"backgroundColor":"#rrggbbaa"?,"align":"left&#124;center&#124;right"?,"anchor":"top&#124;middle&#124;bottom"?,"margin":0..0.45 (fraction of frame height)?,"lineSpacing":f32?,"outline":f32?,"outlineColor":str?,"reset":bool?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.setText</code> | <code>{"caption":id?,"text":str?,"speaker":str&#124;null?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.setTimes</code> | <code>{"caption":id?,"startTime&#124;startFrame&#124;startSeconds&#124;startTimecode":…,"endTime&#124;endFrame&#124;endSeconds&#124;endTimecode":…}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.setTrack</code> | <code>{"track":id&#124;"C1","name":str?,"format":str?,"language":str?,"enabled":bool?,"locked":bool?,"syncLock":bool?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.showActiveOnly</code> | <code>{"track":id&#124;"C1"?}</code> | [sequence_extras.rs](../../../../crates/engine/src/sequence_extras.rs) |
| <code>captions.showAll</code> | <code>{}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.split</code> | <code>{"caption":id?,"time":ticks?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.trim</code> | <code>{"caption":id,"edge":"in&#124;out","delta":ticks&#124;"deltaFrames":i64}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>clip.restoreCaptionsFromSource</code> | <code>{}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
