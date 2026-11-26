# 間・フィラー・話者の選別の設計（ED-43）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

間、指定フィラー、対象話者で候補を抽出し、それぞれ前後の原音を聴いて残す範囲を選択する。

## データと処理境界

候補には基準版・元範囲・保持量・判断を持たせ、適用時に採用区間を元時刻で合成して一度に処理する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/transcript.rs](../../../../crates/engine/src/transcript.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>transcript.removePauses</code> | <code>{"minSeconds":f?,"keepSeconds":f?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
