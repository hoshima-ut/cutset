# 素材・完成版の文字起こしの設計（ED-41）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材またはシーケンス、音声チャンネル、言語、処理範囲を選んで解析し、発言行から対応する音声を開く。

## データと処理境界

語に素材ID・話者ID・元音声区間を結び付ける。シーケンス表示時に配置のトリムと速度を通して表示時刻を求める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/transcript.rs](../../../../crates/engine/src/transcript.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.transcribe</code> | <code>{"track":"mix"&#124;"A1"&#124;id?,"language":"en&#124;auto"?,"diarize":bool?,"maxSpeakers":n?,"model":str?}</code> | [sequence_extras.rs](../../../../crates/engine/src/sequence_extras.rs) |
| <code>transcript.delete</code> | <code>{"items":[id]?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.downloadModel</code> | <code>{"model":"whisper-base"?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.extract</code> | <code>{"from":word,"to":word?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.generate</code> | <code>{"items":[id]?,"model":"whisper-base"?,"language":"en&#124;auto"?,"diarize":bool?,"maxSpeakers":n?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.inspect</code> | <code>{"paragraphGapSeconds":f?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.lift</code> | <code>{"from":word,"to":word?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.models</code> | <code>{}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.removeFillers</code> | <code>{"fillers":[str]?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.renameSpeaker</code> | <code>{"speaker":"Speaker 1"&#124;index,"name":str,"item":id?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.search</code> | <code>{"query":str}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.select</code> | <code>{"from":word,"to":word?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |
| <code>transcript.set</code> | <code>{"item":id,"transcript":{"language":str,"speakers":[{"name":str}],"words":[{"text":str,"start":tick,"end":tick,"speaker":n?}]}}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
