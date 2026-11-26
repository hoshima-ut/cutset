# 挿入・上書きの設計（ED-15）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

挿入先を指定して挿入または上書きを選び、配置後の範囲と後続位置を確認して確定する。

## データと処理境界

挿入は変更範囲の右側を指定尺分移動し、上書きは重なる配置を境界で分割する。対象と同期ロックを一つの編集単位で処理する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/source_placement_tests.rs](../../../../crates/engine/src/source_placement_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>source.insert</code> | <code>{"matchSequence":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>source.overwrite</code> | <code>{"matchSequence":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
