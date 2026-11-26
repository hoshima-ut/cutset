# トラックとバスの設計（AU-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

トラックとサブミックスを接続し、センド位置とバスの行先を選ぶ。ミキサーと出力メーターで信号をたどって確認する。

## データと処理境界

トラック・バス・出力をノード、送りとルーティングを有向辺として持つ。フェーダー前後の各段でセンドを分岐し、重複しない順序で評価する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/mixer.rs](../../../../crates/engine/src/mixer.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>mixer.addInsert</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"effect":str,"slot":n?,"postFader":bool?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.addSend</code> | <code>{"strip":"A1"&#124;"S1"&#124;id,"target":"S1"&#124;id,"levelDb":f64?,"preFader":bool?,"pan":f64?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.addSubmix</code> | <code>{"name":str?,"channels":"Mono&#124;Stereo&#124;5.1"?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.clearLane</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":str?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.deleteKeyframe</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":str?,"time":ticks}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.deleteSubmix</code> | <code>{"strip":"S1"&#124;id}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.inspect</code> | <code>{"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.moveKeyframe</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":str?,"time":ticks,"newTime":ticks?,"value":f64?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.recordStart</code> | <code>{"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.recordStop</code> | <code>{"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.release</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":str?,"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.removeInsert</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"slot":n}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.removeSend</code> | <code>{"strip":"A1"&#124;"S1"&#124;id,"send":n}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.setInsert</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"slot":n,"enabled":bool?,"postFader":bool?,"params":{id:value}?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.setKeyframe</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":str?,"time":ticks?,"value":f64}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.setSend</code> | <code>{"strip":"A1"&#124;"S1"&#124;id,"send":n,"levelDb":f64?,"pan":f64?,"preFader":bool?,"muted":bool?,"target":"S1"?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.setStrip</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"name":str?,"volumeDb":f64?,"pan":f64?,"muted":bool?,"solo":bool?,"recordArm":bool?,"soloSafe":bool?,"mode":"Off&#124;Read&#124;Latch&#124;Touch&#124;Write"?,"output":"Mix"&#124;"S1"?,"inputMap":"Stereo&#124;Left&#124;Right&#124;Swap&#124;Mono"?,"channels":"Mono&#124;Stereo&#124;5.1"?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.setValue</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":"volume&#124;pan&#124;mute&#124;send.&lt;i&gt;.level&#124;fx.&lt;slot&gt;.&lt;param&gt;","value":f64,"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.touch</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":"volume&#124;pan&#124;mute&#124;send.&lt;i&gt;.level&#124;fx.&lt;slot&gt;.&lt;param&gt;","value":f64,"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>mixer.writeAutomation</code> | <code>{"strip":"A1"&#124;"S1"&#124;"Mix"&#124;id,"lane":str?,"points":[[ticks,value]],"tolerance":f64?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
