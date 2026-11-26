# IO-54 編集決定リスト — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象トラック、リールの命名、タイムコード形式を指定し、EDLのイベントと変換損失を確認する。

## データと処理境界

各イベントにリール名、素材In/Out、記録側In/Out、遷移種別を割り当て、イベント順で出力する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/interchange/src/edl.rs](../../../../crates/interchange/src/edl.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportEdl</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
