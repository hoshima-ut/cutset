# GR-01 画面上の文字組み — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

画面上に点文字または段落枠を作り、日本語IME入力を確定してから書体・字間・行幅を変える。あふれた行を枠内で識別できる。

## データと処理境界

文字列、段落枠と行組み、書体参照、塗りと縁取りをレイヤーに保持する。組版結果をモニターとレンダーで共有し、未確定文字列は編集セッションで扱う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphics.rs](../../../../crates/engine/src/graphics.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.replaceFonts</code> | <code>{"from":family&#124;{"family","style"?},"to":family&#124;{"family","style"?},"toStyle":str?}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>fonts.list</code> | <code>{"system":bool=true (scan the system font folders)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignTextCenter</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.alignTextLeft</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.alignTextRight</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.fontSizeDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.fontSizeDown5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.fontSizeUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.fontSizeUp5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.fonts.used</code> | <code>{}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.leadingDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.leadingDown5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.leadingUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.leadingUp5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>graphics.newText</code> | <code>{"text":str="New Text","position":[x,y]? (point text: its alignment point on the first baseline; with `box`: the box's top-left corner),"box":[w,h]? (paragraph text wrapped in a box this size),"clip":id?,"newClip":bool?,"vertical":bool=false,"size":px=100,"font":str?,"fontStyle":str?,"seconds":f64=5,"track":index?,"time":ticks?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.newVerticalText</code> | <code>{"text":str="New Text","position":[x,y]?,"clip":id?,"size":px=100,"seconds":f64=5,"time":ticks?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.setCharStyle</code> | <code>{"clip":id?,"layer":n&#124;name?,"start":char=0,"end":char=len,"style":{"font":str,"fontStyle":str,"size":px,"color":"#rrggbb","stroke":bool,"strokeColor":"#rrggbb","strokeWidth":px,"strokeType":"outer&#124;center&#124;inner","stroke2":bool,"stroke2Color":"#rrggbb","stroke2Width":px,"stroke2Type":"outer&#124;center&#124;inner","bold":bool,"italic":bool,"underline":bool,"strikethrough":bool,"tracking":n,"baselineShift":px,"caps":"normal&#124;all caps&#124;small caps"},"clear":bool? (remove styles from the range),"merge":bool?,"begin":bool? (start a new undo gesture)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.setText</code> | <code>{"clip":id?,"layer":n&#124;name?,"text":str,"merge":bool? (coalesce with the previous Edit Text undo step)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.setTextType</code> | <code>{"clip":id?,"layer":n&#124;name?,"type":"point&#124;paragraph" (point: no box, handles scale the text; paragraph: the text wraps in a box that handles resize)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
