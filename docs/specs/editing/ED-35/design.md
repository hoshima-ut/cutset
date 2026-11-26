# ED-35 静止フレーム — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

保持する元フレームを選び、区間として挿入するか対象全体を静止させるかを指定する。

## データと処理境界

保持元は素材IDと素材フレーム番号で記録し、表示ヘッドを動かしても変えない。字幕・別トラックの音声の扱いは対象選択に従う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/clip_ops_tests.rs](../../../../crates/engine/src/clip_ops_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.frameHold</code> | <code>{"clips":[id]?,"time":ticks?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.frameHoldOptions</code> | <code>{"clips":[id]?,"enabled":bool=true,"holdOn":"sourceTimecode&#124;sequenceTime&#124;in&#124;out&#124;playhead"?,"time":ticks?,"timecode":str?,"holdFilters":bool=false}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.insertFrameHoldSegment</code> | <code>{"clip":id?,"time":ticks?,"seconds":f64=2}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
