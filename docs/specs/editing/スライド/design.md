# スライドの設計（ED-30）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

隣り合う3配置の中央を選び、中央の内容を保ったまま配置位置を動かす。

## データと処理境界

中央の素材範囲と長さを固定し、前の終端と後ろの開始を移動量に合わせる。3配置の外端を固定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/slip.rs](../../../../crates/engine/src/slip.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>timeline.slide</code> | <code>{"clip":id,"delta":ticks&#124;"deltaFrames":i64}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.slideLeft</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.slideLeft5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.slideRight</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>timeline.slideRight5</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
