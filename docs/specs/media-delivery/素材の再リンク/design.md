# 素材の再リンクの設計（IO-23）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

欠落素材を選び、探索先の候補を尺・識別情報・試聴画で比較して再接続する。

## データと処理境界

素材IDは維持し、承認済みの参照先と検査結果のみ更新する。連動する全配置が同じ原本へ解決する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/relink.rs](../../../../crates/engine/src/relink.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>media.autoRelink</code> | <code>{"from":str,"to":str}&#124;{"folder":str} + match options</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.findMissing</code> | <code>{}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.linkMedia</code> | <code>{}  (opens the Link Media dialog; agents use media.relink / media.autoRelink)</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.makeOffline</code> | <code>{"items":[id]?,"deleteFiles":bool=false}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.offlineAll</code> | <code>{}  (mark every missing file offline, saved with the project, and close the Link Media dialog)</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.refreshChanged</code> | <code>{}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.relink</code> | <code>{"item":id,"path":str,"force":bool=false,"relinkOthers":bool=true,"alignTimecode":bool=false,"match":{"fileName":bool,"extension":bool,"clipId":bool,"duration":bool,"mediaStart":bool,"metadata":bool}?}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.replaceFootage</code> | <code>{"item":id,"path":str}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.search</code> | <code>{"folder":str,"item":id?,"exactName":bool=true}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |
| <code>media.status</code> | <code>{"item":id?}</code> | [relink.rs](../../../../crates/engine/src/relink.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
