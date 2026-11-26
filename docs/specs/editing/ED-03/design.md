# ED-03 ビンと絵コンテ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

ビンで素材を自由配置し、サムネイル順、名前順、手動選択順を切り替え、必要な順序を一括配置に渡す。

## データと処理境界

ビン内の項目IDと表示座標・ソートを分離する。タイムラインには一括配置を確定した時点の順序と個別の配置IDを記録する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_panel.rs](../../../../crates/engine/src/project_panel.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>project.columns.list</code> | <code>{}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.columns.resize</code> | <code>{"column":str,"width":f32}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.columns.set</code> | <code>{"columns":[name&#124;{"name":str,"width":f32}]}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.delete</code> | <code>{"items":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>project.deselectAll</code> | <code>{}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.alignToGrid</code> | <code>{"bin":binId?,"grid":f32?,"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.arrangements</code> | <code>{"bin":binId?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.deleteArrangement</code> | <code>{"name":str,"bin":binId?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.layout</code> | <code>{"bin":binId?,"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.move</code> | <code>{"items":[id]?,"x":f32,"y":f32,"snap":bool?,"width":f32?} &#124; {"positions":{"&lt;id&gt;":[x,y]},"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.options</code> | <code>{"grid":f32?,"snap":bool?,"showNames":bool?,"showDurations":bool?,"cardSize":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.reset</code> | <code>{"bin":binId?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.resize</code> | <code>{"items":[id]?,"size":f32?,"step":1&#124;-1?,"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.restoreArrangement</code> | <code>{"name":str,"bin":binId?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.saveArrangement</code> | <code>{"name":str,"bin":binId?,"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.stack</code> | <code>{"items":[id]?,"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.freeform.unstack</code> | <code>{"items":[id]?,"width":f32?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.inspect</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>project.items</code> | <code>{"bin":binId?,"recursive":bool?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.matteColor</code> | <code>{"item":id?,"color":"#rrggbb"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>project.moveToBin</code> | <code>{"items":[id&#124;binId]?,"bin":binId&#124;null}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>project.notes</code> | <code>{}</code> | [panels.rs](../../../../crates/engine/src/panels.rs) |
| <code>project.renameBin</code> | <code>{"bin":binId,"name":str}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.select</code> | <code>{"items":[id]}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>project.selectAll</code> | <code>{"bin":binId?,"expanded":[binId]?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.setMarks</code> | <code>{"item":id,"in":ticks?&#124;null,"out":ticks?&#124;null}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>project.setNotes</code> | <code>{"text":str,"merge":str?}</code> | [panels.rs](../../../../crates/engine/src/panels.rs) |
| <code>project.sort</code> | <code>{"column":str,"descending":bool?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.view.get</code> | <code>{}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.view.set</code> | <code>{"view":"list&#124;icon&#124;freeform"?,"iconSize":f32?,"fontSize":"small&#124;medium&#124;large&#124;extraLarge"?,"previewArea":bool?,"thumbnails":bool?,"thumbnailsShowEffects":bool?,"hoverScrub":bool?,"thumbnailControlsAllDevices":bool?,"iconSort":column&#124;{"column":str,"descending":bool}?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.viewPreset.delete</code> | <code>{"slot":1..10}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.viewPreset.list</code> | <code>{}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.viewPreset.rename</code> | <code>{"slot":1..10,"name":str}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.viewPreset.restore</code> | <code>{"slot":1..10}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.viewPreset.save</code> | <code>{"slot":1..10?,"name":str?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |
| <code>project.viewPreset.saveAs</code> | <code>{"name":str?,"slot":1..10?}</code> | [project_panel.rs](../../../../crates/engine/src/project_panel.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
