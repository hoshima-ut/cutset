# UI-04 キーの割当と競合 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

割当検索でキーまたは操作名を入力し、適用面と衝突先を確認して上書きまたは取消を選ぶ。

## データと処理境界

割当は命令ID、修飾キー、物理キーまたは文字キー、適用コンテキストを組にする。文字入力とIME変換中は該当ウィジェットを優先する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/shortcuts.rs](../../../../crates/engine/src/shortcuts.rs)。

確認した関数：[conflicts](../../../../crates/engine/src/shortcuts.rs)。既存の割当表はOSごとに競合キーを列挙し、再割当で置き換えた命令を返す。字幕入力中のDeleteとIME変換は実際のフォーカスを通して別途確認する。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>shortcuts.audit</code> | <code>{}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.clear</code> | <code>{"command":id,"keys":str?,"panel":str?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.conflicts</code> | <code>{"platform":"mac&#124;windows&#124;linux"?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.deletePreset</code> | <code>{"name":str}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.export</code> | <code>{"path":str}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.forKey</code> | <code>{"key":"K","platform":str?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.get</code> | <code>{"command":id,"platform":str?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.import</code> | <code>{"path":str,"activate":bool=true}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.list</code> | <code>{"query":str?,"panel":str?,"assigned":bool?,"platform":"mac&#124;windows&#124;linux"?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.loadPreset</code> | <code>{"name":str}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.presets</code> | <code>{}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.redo</code> | <code>{}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.resolve</code> | <code>{"keys":str,"panel":str?,"platform":str?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.savePreset</code> | <code>{"name":str}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.set</code> | <code>{"command":id,"keys":"Cmd+Shift+K","panel":str?,"add":bool?,"keepConflicts":bool?}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |
| <code>shortcuts.undo</code> | <code>{}</code> | [shortcuts.rs](../../../../crates/engine/src/shortcuts.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
