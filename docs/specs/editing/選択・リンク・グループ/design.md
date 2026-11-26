# 選択・リンク・グループの設計（ED-18）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

配置を単独選択・追加選択し、リンク選択とグループ移動を切り替えて、動く配置を先に表示する。

## データと処理境界

選択集合、同期リンク、グループ所属は別に管理する。操作は素材IDではなく配置IDで解決し、同じ素材の別使用箇所を巻き込まない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/clip_ops.rs](../../../../crates/engine/src/clip_ops.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.clearPosterFrame</code> | <code>{"item":id?}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.editOffline</code> | <code>{"item":id?,"mediaName":str?,"tapeName":str?,"description":str?,"scene":str?,"shot":str?,"logNote":str?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>clip.editSubclip</code> | <code>{"item":id?,"start":ticks?,"end":ticks?,"startFrame":i64?,"endFrame":i64?,"restrictTrims":bool?,"convertToMaster":bool?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.enable</code> | <code>{"clips":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.generateAudioWaveform</code> | <code>{"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>clip.group</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.link</code> | <code>{"clips":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.makeSubclip</code> | <code>{"item":id?,"clip":id?,"name":str?,"start":ticks?,"end":ticks?,"startFrame":i64?,"endFrame":i64?,"restrictTrims":bool=true}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.rename</code> | <code>{"clip":id?,"clips":[id]?,"item":id?,"name":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.revealInProject</code> | <code>{"clip":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.setPosterFrame</code> | <code>{"item":id?,"time":ticks?}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.sourceSettings</code> | <code>{"item":id?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>clip.ungroup</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.copy</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.deselectAll</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.duplicate</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.editOriginal</code> | <code>{"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>edit.find</code> | <code>{"scope":"project&#124;timeline"?,"column":str?,"operator":"contains&#124;matches&#124;beginsWith&#124;endsWith&#124;doesNotContain"?,"text":str?,"rows":[{"column":str,"operator":str,"text":str}]?,"matchAll":bool=true,"caseSensitive":bool=false,"in":"all&#124;clips&#124;markers"?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>edit.findNext</code> | <code>{}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>edit.paste</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.pasteInsert</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.pasteMedia</code> | <code>{"paths":[str],"insert":bool?,"place":bool=true,"bin":binId?}</code> | [paste_media.rs](../../../../crates/engine/src/paste_media.rs) |
| <code>edit.selectAll</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.selectAllMatching</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>timeline.select</code> | <code>{"clips":[id],"transitions":[id]?,"add":bool,"toggle":bool,"linked":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.selectClipAtPlayhead</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.selectGap</code> | <code>{"track":"V1"&#124;id,"time":ticks&#124;"frame":n&#124;"seconds":f}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.selectNextClip</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.selectPrevClip</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
