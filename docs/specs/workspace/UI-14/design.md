# UI-14 設定の保存範囲 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

設定を選ぶと保存先と適用範囲を示す。変更・既定値復帰の対象範囲を選んで確定する。

## データと処理境界

ユーザー設定、案件設定、シーケンス設定にそれぞれ所有者を持たせ、同名項目の有効値と出所を表示する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/settings.rs](../../../../crates/engine/src/settings.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>prefs.get</code> | <code>{"key":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>prefs.reset</code> | <code>{"category":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>prefs.schema</code> | <code>{"category":str?}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |
| <code>prefs.set</code> | <code>{"key":str,"value":any}&#124;{"values":{key:value}}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
