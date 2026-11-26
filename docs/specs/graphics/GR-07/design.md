# GR-07 タイトルテンプレート — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

テンプレートのサムネイルと依存素材を確認して配置する。編集欄には公開された文字・色等のコントロールを表示する。

## データと処理境界

テンプレートID・版と、配置ごとの公開値を区別する。入力の型・範囲・既定値を検証し、内部レイヤーはテンプレート側で評価する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportGraphicsTemplate</code> | <code>as graphics.template.export</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.apply</code> | <code>{"template":id&#124;name&#124;path,"values":{control id or name: value}?,"time":ticks?,"track":index?}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.controls</code> | <code>{"clip":id?}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.export</code> | <code>{"clip":id?,"name":str,"category":str="My Templates","description":str?,"controls":[{"layer":n&#124;name,"param":"text&#124;fill_color&#124;size&#124;font&#124;position&#124;enabled&#124;…","name":str?,"kind":"text&#124;color&#124;slider&#124;checkbox&#124;font&#124;position"?,"min":f64?,"max":f64?,"id":str?}]? (default: each text layer's text),"path":str? (default: the user templates folder),"embedFonts":bool=false,"fontLicense":str?}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.install</code> | <code>{"path":str (a .fcgt file; Adobe .mogrt files are refused)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.list</code> | <code>{"query":str? (search names, categories, descriptions, tags),"category":str?,"source":"builtin&#124;user"?}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.remove</code> | <code>{"template":id&#124;name (a user template)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.set</code> | <code>{"clip":id?,"control":id&#124;name,"value":any} or {"clip":id?,"values":{control: value}}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.template.thumbnail</code> | <code>{"template":id&#124;name&#124;path,"width":px=320,"path":str? (write a PNG there; else returned as pngBase64)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
