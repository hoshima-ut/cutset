# IO-15 ビンの整理 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

ビンを選び、列やサムネイル表示で内容を整理する。使用箇所の行からシーケンス内の配置へ移動する。

## データと処理境界

所属は親ビンIDで表し、表示名や並べ替え順を変更しても素材IDと配置の参照を維持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_panel.rs](../../../../crates/engine/src/project_panel.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.newBin</code> | <code>{"name":str,"parent":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newBinFromSelection</code> | <code>{"items":[id]?,"name":str?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>file.newSearchBin</code> | <code>{"name":str?,"column":str?,"operator":str?,"text":str?,"rows":[..]?,"matchAll":bool?,"caseSensitive":bool?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
