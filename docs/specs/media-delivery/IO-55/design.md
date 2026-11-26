# IO-55 音声ポスト受け渡し — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

音声編集先に合わせてAAFまたはOMFと受渡方向を選び、埋込み・外部音声・ハンドルを確認する。

## データと処理境界

各トラックの開始位置、素材範囲、ソースチャンネル、サンプルレート、要求ハンドルと実際に確保できた長さを記録する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/aaf_omf.rs](../../../../crates/engine/src/aaf_omf.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportAaf</code> | <code>{"path":str,"sequence":id?,"mixdownVideo":bool?,"mixdownFormat":"mov&#124;mxf"?,"breakoutToMono":bool?,"audio":"embedded&#124;separate&#124;linked"?,"audioFormat":"wav&#124;aiff&#124;mxf"?,"sampleRate":int?,"bitDepth":"16&#124;24"?,"trimAudio":bool?,"handles":frames?,"renderAudioEffects":bool?,"smallSectors":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.exportOmf</code> | <code>{"path":str,"sequence":id?,"title":str?,"audio":"embedded&#124;separate"?,"audioFormat":"wav&#124;aiff"?,"sampleRate":int?,"bitDepth":"16&#124;24"?,"trimAudio":bool?,"handles":frames?,"renderAudioEffects":bool?,"breakoutToMono":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.importAaf</code> | <code>{"path":str,"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
