# IO-48 書き出しキュー — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

出力設定を確定してキューに登録し、待機・実行中・中止・失敗・完了をジョブごとに表示する。

## データと処理境界

ジョブIDと案件版、範囲、出力先、実効設定を保存する。完成品は成功後に所定のファイル名で公開する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/export_mode/queue.rs](../../../../crates/ui-egui/src/panels/export_mode/queue.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>export.queue.add</code> | <code>{…settings params,"path":str&#124;dir?,"sequences":[id]?,"ranges":[range]?,"start":bool?,"wait":bool?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.cancel</code> | <code>{"id":id?,"wait":bool?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.clear</code> | <code>{"all":bool=false}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.list</code> | <code>{}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.move</code> | <code>{"id":id,"to":index?,"by":int?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.remove</code> | <code>{"id":id}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.retry</code> | <code>{"id":id,"start":bool?,"wait":bool?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.start</code> | <code>{"wait":bool=false}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.queue.stop</code> | <code>{}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
