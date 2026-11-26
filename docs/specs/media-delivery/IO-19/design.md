# IO-19 メタデータ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

属性を開き、案件だけに保存する欄とファイルに反映する欄を確認して更新する。

## データと処理境界

案件の項目IDに属する値と、元ファイルまたはサイドカーに属する値を分離する。書込先と結果を返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/metadata.rs](../../../../crates/ui-egui/src/panels/metadata.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.updateMetadata</code> | <code>{"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>metadata.get</code> | <code>{"item":id?,"clip":id?}</code> | [panels.rs](../../../../crates/engine/src/panels.rs) |
| <code>metadata.set</code> | <code>{"item":id?,"clip":id?,"field":"Name&#124;Label&#124;Description&#124;Scene&#124;Shot&#124;Log Note&#124;Comment&#124;Tape Name&#124;Client&#124;Camera Angle&#124;…","value":str} &#124; {"item":id?,"fields":{name:str}}</code> | [panels.rs](../../../../crates/engine/src/panels.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
