# AU-04 クリップゲイン — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

選択した配置の現在ゲインと測定ピークを表示し、絶対指定・相対加算・ピーク正規化を選ぶ。複数配置では共通補正か各自補正かを明示する。

## データと処理境界

dBの調整量を配置単位で保持し、分析ピークは素材・範囲と紐づける。適用時に元の波形と既存ゲインを区別して目標との差分を求める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/timeline_volume.rs](../../../../crates/ui-egui/src/panels/timeline_volume.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.audioGain</code> | <code>{"clips":[id]?,"mode":"set&#124;adjust&#124;normalizeMax&#124;normalizeAll"?,"db":f64,"relative":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.audioPeak</code> | <code>{"clips":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.nudgeVolumeDown1</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.nudgeVolumeDown3</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.nudgeVolumeUp1</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.nudgeVolumeUp3</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.volumeDown</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.volumeDownMany</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.volumeUp</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>clip.volumeUpMany</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
