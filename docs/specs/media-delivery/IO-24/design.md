# IO-24 プロキシの生成 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象動画とプロキシプリセットを選び、生成進捗を表示する。完了時に対象の素材へ割り当てる。

## データと処理境界

素材ID、原本の識別情報、プリセットを生成依頼に持たせる。完了ファイルを検査してから対応を保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/proxies.rs](../../../../crates/engine/src/proxies.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>media.attachProxies</code> | <code>{"item":id,"path":str}&#124;{"items":[id],"paths":[str]},"force":bool=false</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |
| <code>media.createProxies</code> | <code>{"items":[id]?,"preset":"prores_proxy_quarter&#124;prores_proxy_half&#124;prores_lt_half&#124;h264_quarter&#124;h264_half"?,"destination":str?,"attach":bool=true,"wait":bool=false}</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |
| <code>media.detachProxies</code> | <code>{"items":[id]?}</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |
| <code>media.proxyPresets</code> | <code>{}</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |
| <code>media.reconnectFullRes</code> | <code>{"item":id,"path":str}</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |
| <code>media.toggleProxies</code> | <code>{"enabled":bool?}</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
