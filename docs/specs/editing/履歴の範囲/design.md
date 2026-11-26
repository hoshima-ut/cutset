# 履歴の範囲の設計（ED-59）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

履歴一覧で現在の編集取引の前後を確認し、別途保存済みの世代を選んで開く。表示変更は編集のUndoに含めない。

## データと処理境界

Undoスタックは現在の編集セッション、表示設定は端末、復旧世代は保存先が所有する。新規編集時のRedoクリアと履歴の起点を見せる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/history_tests.rs](../../../../crates/engine/src/history_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>history.clear</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>history.deleteRedoable</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>history.list</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
