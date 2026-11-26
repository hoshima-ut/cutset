# GR-02 図形・画像レイヤー — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

グラフィック配置に図形・画像を追加し、レイヤー欄で重なりを変える。グループを選んで移動した後、単独レイヤーの塗りを編集する。

## データと処理境界

ペイント順、レイヤーID、グループ内座標、画像の素材参照を保持する。グラデーション停止点とアルファをレイヤーの描画時に評価する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphics.rs](../../../../crates/engine/src/graphics.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>graphics.arrangeLayer</code> | <code>{"clip":id?,"layer":n?,"to":"front&#124;back&#124;forward&#124;backward"&#124;index}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.deleteLayer</code> | <code>{"clip":id?,"layer":n?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.list</code> | <code>{"clip":id?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.moveLayers</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers),"delta":[dx,dy] (graphic pixels)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.newEllipse</code> | <code>{"position":[x,y]?,"size":[w,h]=[400,200],"clip":id?,"seconds":f64=5,"track":index?,"time":ticks?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.newFromFile</code> | <code>{"path":str,"time":ticks?,"track":index?} (imports the image or video and places it above the clips at the playhead)</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.newPolygon</code> | <code>{"position":[x,y]?,"size":[w,h]=[300,300],"sides":n=6,"clip":id?,"seconds":f64=5,"track":index?,"time":ticks?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.newRectangle</code> | <code>{"position":[x,y]?,"size":[w,h]=[400,200],"clip":id?,"seconds":f64=5,"track":index?,"time":ticks?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.newShape</code> | <code>{"shape":"rectangle&#124;ellipse&#124;polygon&#124;path","position":[x,y]? (the shape's centre),"size":[w,h]=[400,200],"points":[[x,y],…]?,"clip":id? (add the shape to this graphic),"seconds":f64=5,"track":index?,"time":ticks?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.nudgeDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeDown5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeLeft</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeLeft5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeRight</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeRight5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.nudgeUp5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.resetAllParameters</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers, else all)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.resetDuration</code> | <code>{"clip":id?,"seconds":f64=5 (the default graphic duration; limited by the next clip on the track)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.selectLayer</code> | <code>{"clip":id?,"layers":[n]}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.selectNextGraphic</code> | <code>{}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.selectNextLayer</code> | <code>{}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.selectPreviousGraphic</code> | <code>{}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.selectPreviousLayer</code> | <code>{}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.set</code> | <code>{"clip":id?,"clips":[id]? (instead of `clip`: the same props on that layer of each listed graphic clip, as one undo step),"layer":n&#124;name?,"props":{"font":"Inter","font_style":"Bold","size":120,"align":"center","tracking":50,"leading":0,"fill_color":"#ffcc00","stroke":true,"stroke_width":6,"background":true,"shadow":true,"position":[x,y],"scale":100,"rotation":0,"opacity":100,…},"time":ticks? (timeline time, default the playhead: a property that is already animated gets or changes a keyframe there, any other changes its fixed value),"keyframe":bool? (true: every property in `props` gets a keyframe at `time` and becomes animated; the result lists each one's keyframe count),"merge":bool?,"begin":bool?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.upgradeCaption</code> | <code>{"captions":[id]? (default: the selected captions, else the one under the playhead)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.upgradeToSourceGraphic</code> | <code>{"clip":id?}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
