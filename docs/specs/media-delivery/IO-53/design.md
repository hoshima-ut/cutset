# IO-53 XML交換 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

書き出すXML方言と版を選び、受け手で開いた結果と変換ログを照合する。

## データと処理境界

FCP 7 XMLとFCPXMLを別の変換器で処理し、各方言の時刻表現から素材範囲とシーケンス位置を変換する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/interchange/src/fcp7.rs](../../../../crates/interchange/src/fcp7.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportFcp7Xml</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.exportFcpxml</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
