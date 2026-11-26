# IO-13 ナレーションの取り込み — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

入力デバイスとチャンネル、録音先、開始位置を選ぶ。録音、停止、ファイル確定の順に進める。

## データと処理境界

入力音は選択トラックの新規素材として登録する。入力の録音ゲイン、モニターミュート、再生ミックスを別々に扱う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/voiceover.rs](../../../../crates/engine/src/voiceover.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>audio.voiceover.settings</code> | <code>{"source":str?,"inputChannel":n?,"name":str?,"countdownSoundCues":bool?,"prerollSeconds":f64?,"postrollSeconds":f64?}</code> | [voiceover.rs](../../../../crates/engine/src/voiceover.rs) |
| <code>audio.voiceover.start</code> | <code>{"track":"A1"&#124;id?,"time":ticks?,"preroll":seconds?}</code> | [voiceover.rs](../../../../crates/engine/src/voiceover.rs) |
| <code>audio.voiceover.stop</code> | <code>{"time":ticks?,"dir":str?,"discard":bool?}</code> | [voiceover.rs](../../../../crates/engine/src/voiceover.rs) |
| <code>audio.voiceover.sync</code> | <code>{"time":ticks?}</code> | [voiceover.rs](../../../../crates/engine/src/voiceover.rs) |
| <code>tts.create</code> | <code>{"text":str,"voice":str?,"pitch":"extraLow&#124;low&#124;default&#124;high&#124;extraHigh"?,"pace":0.5..2?,"time":ticks?,"track":"A1"&#124;id?,"dir":str?}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |
| <code>tts.downloadVoices</code> | <code>{"wait":bool?}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |
| <code>tts.edit</code> | <code>{"clip":id?,"text":str?,"voice":str?,"pitch":str?,"pace":f64?,"dir":str?}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |
| <code>tts.inspect</code> | <code>{"clip":id?,"item":id?}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |
| <code>tts.preview</code> | <code>{"text":str?,"voice":str?,"pitch":"default"?,"pace":f64?,"sample":bool?,"clip":id?,"path":str?}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |
| <code>tts.render</code> | <code>{"text":str?,"voice":str?,"pitch":str?,"pace":f64?,"sample":bool?,"clip":id?,"wait":bool?}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |
| <code>tts.voices</code> | <code>{}</code> | [narration.rs](../../../../crates/engine/src/narration.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
