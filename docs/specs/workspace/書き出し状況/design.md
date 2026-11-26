# 書き出し状況の設計（UI-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

出力範囲と対象版を確認してキューへ追加し、ジョブ詳細で進捗・中止・再試行を操作する。

## データと処理境界

ジョブIDに入力版、開始・終端、映像・音声・字幕の設定、出力先と状態を結び付ける。再試行の入力版を明示する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/export_mode/queue.rs](../../../../crates/ui-egui/src/panels/export_mode/queue.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>jobs.cancel</code> | <code>{"job":id}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>jobs.list</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
