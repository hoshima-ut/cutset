# 重複と条件検索の設計（IO-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

条件検索の結果を開き、重複候補と使用箇所を比較してから統合する。

## データと処理境界

検索ビンは条件を保持する。統合時は確認済みの同一素材を指す参照だけを代表項目へ付け替える。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/media_pool.rs](../../../../crates/engine/src/media_pool.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>edit.consolidateDuplicates</code> | <code>{}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.removeUnused</code> | <code>{}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>project.deleteSearchBin</code> | <code>{"bin":id}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>project.editSearchBin</code> | <code>{"bin":id,"name":str?,"column":str?,"operator":str?,"text":str?,"rows":[..]?,"matchAll":bool?,"caseSensitive":bool?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>project.searchBinItems</code> | <code>{"bin":id}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
