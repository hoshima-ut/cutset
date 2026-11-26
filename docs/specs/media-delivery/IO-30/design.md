# IO-30 保存と案件切替 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

未保存の変更を案件ごとに示し、保存・切替・終了を選ぶ。異常終了後は復旧版の日時と元の保存版を比較する。

## データと処理境界

案件IDごとに保存先、変更版、自動保存世代を管理する。書込が完了してから保存済み扱いに切り替える。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/autosave.rs](../../../../crates/engine/src/autosave.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.close</code> | <code>{"item":id?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.closeAllOtherProjects</code> | <code>{}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.closeAllProjects</code> | <code>{"force":bool?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.closeProject</code> | <code>{"force":bool?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>file.mediaProperties</code> | <code>{"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.mediaPropertiesFile</code> | <code>{"path":str}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.open</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.openDemoProject</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.projectSettings.general</code> | <code>{"renderer":"gpu&#124;software"?,"videoDisplay":"timecode&#124;feet35&#124;feet16&#124;frames"?,"audioDisplay":"samples&#124;milliseconds"?,"captureFormat":"DV&#124;HDV"?,"titleSafe":[h,v]?,"actionSafe":[h,v]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.projectSettings.scratchDisks</code> | <code>{"captured":path&#124;null?,"videoPreviews":path&#124;null?,"audioPreviews":path&#124;null?,"autoSave":path&#124;null?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.reveal</code> | <code>{"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.revert</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.save</code> | <code>{"path":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.saveAll</code> | <code>{}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>file.saveAs</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.saveAsTemplate</code> | <code>{"name":str?,"path":str?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.saveCopy</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.templates</code> | <code>{}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
