# ED-05 フレーム送りとシャトル — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

再生するモニターを選び、コマ送り、逆送り、シャトル速度の変更、指定範囲のループを行う。

## データと処理境界

送り量は表示フレーム境界で算出する。モニターの再生方向・速度・範囲は案件のクリップ速度から独立させる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)、[crates/ui-egui/src/source_playback.rs](../../../../crates/ui-egui/src/source_playback.rs)。

確認した関数：[shuttle_source](../../../../crates/ui-egui/src/source_playback.rs)。素材用の正逆シャトルを実装済み。既存試験はJ/Lの方向と倍速化を扱う。完成側との切替後の位置と納品結果は試験を分ける。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>audio.toggleScrubbing</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>playhead.end</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.nextEdit</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.nextEditAnyTrack</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>playhead.prevEdit</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.prevEditAnyTrack</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>playhead.selectedClipEnd</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>playhead.selectedClipStart</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |
| <code>playhead.set</code> | <code>{"time":ticks&#124;"frame":i64&#124;"seconds":f64&#124;"timecode":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.start</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.step</code> | <code>{"frames":i64}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.stepBack</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.stepBack5</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.stepForward</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>playhead.stepForward5</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
