# UI-17 欠落素材と音の診断 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

オフライン配置または無音のトラックを選び、素材、デコード、トラック、ミキサー、モニター出力の順に調べる。

## データと処理境界

配置と素材の参照を保持し、エラーには発生段階と対象IDを付ける。再リンク後は該当する波形とプレビューを更新する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/relink.rs](../../../../crates/engine/src/relink.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>events.clear</code> | <code>{}</code> | [panels.rs](../../../../crates/engine/src/panels.rs) |
| <code>events.list</code> | <code>{"level":"info&#124;warning&#124;error"?,"since":id?}</code> | [panels.rs](../../../../crates/engine/src/panels.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
