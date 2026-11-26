# IO-41 出力プリセット — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

出力形式を選んでプリセットを適用し、個別の上書きと最終値を確認する。簡易書き出しでも適用先を表示する。

## データと処理境界

プリセットの識別子・版と解決済みの設定を分離する。キューへの登録時に解像度、音声、色、範囲を固定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/export/src/presets.rs](../../../../crates/export/src/presets.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>export.formats</code> | <code>{}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.delete</code> | <code>{"name":str}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.export</code> | <code>{"path":str,"names":[str]?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.favorite</code> | <code>{"name":str,"favorite":bool?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.get</code> | <code>{"name":str}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.import</code> | <code>{"path":str}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.list</code> | <code>{"query":str?,"category":str?,"format":str?,"favorites":bool?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.presets.save</code> | <code>{"name":str,"from":str?,"settings":ExportSettings?,"category":str?,"description":str?,"overwrite":bool=true, …flat overrides}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.quick</code> | <code>{"preset":str?,"path":str?,"wait":bool?, …settings params}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |
| <code>export.resolve</code> | <code>{…settings params, "path":str?}</code> | [export_tools.rs](../../../../crates/engine/src/export_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
