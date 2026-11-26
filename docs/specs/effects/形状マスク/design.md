# 形状マスクの設計（FX-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

マスクの所属先を不透明度または特定効果に指定し、輪郭を描く。反転、フェザー、拡張の順にプレビューして形状を確定する。

## データと処理境界

輪郭頂点、制御点、フェザー量・拡張量、適用先IDを保持し、画素ごとの被覆率を返す。不透明度ではアルファ、効果では処理前後の混合に使用する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/masks.rs](../../../../crates/engine/src/masks.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>masks.add</code> | <code>{"clip":id?,"effect":index&#124;id?="opacity","shape":"ellipse"&#124;"polygon"&#124;"rectangle"&#124;"bezier","path":[[x,y]…]&#124;{vertices}?,"center":[x,y]?,"size":[w,h]?,"cornerRadius":px?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.addVertex</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"after":n,"at":[x,y]}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.list</code> | <code>{"clip":id?,"time":ticks?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.moveVertex</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"vertex":n&#124;"vertices":[n],"handle":"point"&#124;"in"&#124;"out"?,"to":[x,y]?&#124;"delta":[dx,dy]?,"breakHandles":bool?,"merge":key?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.remove</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.removeVertex</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"vertex":n}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.roundCorners</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"radius":px,"vertices":[n]?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.select</code> | <code>{"clip":id,"effect":index&#124;id,"mask":n}&#124;{"none":true}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.set</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"name":str?,"inverted":bool?,"mode":"none&#124;add&#124;subtract&#124;intersect&#124;lighten&#124;darken&#124;difference"?,"trackMethod":"position&#124;positionRotation&#124;positionScaleRotation"?,"feather":px?,"opacity":pct?,"expansion":px?,"path":path?,"time":ticks?,"merge":key?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.toggleVertexSmooth</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"vertex":n}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.track</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"direction":"forward"&#124;"backward"?,"frames":n?,"method":"position&#124;positionRotation&#124;positionScaleRotation"?,"wait":bool?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |
| <code>masks.translate</code> | <code>{"clip":id?,"effect":index&#124;id?,"mask":n?,"delta":[dx,dy],"merge":key?}</code> | [masks.rs](../../../../crates/engine/src/masks.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
