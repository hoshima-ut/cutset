# 配置の効果スタックの設計（FX-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

クリップの効果欄で追加、並べ替え、有効切替を行い、指定フレームのプレビューを更新する。属性貼付は適用先と対象属性を確認して確定する。

## データと処理境界

配置IDごとに順序付きの効果インスタンスを保持する。複写先には別のインスタンスIDを割り当て、各効果の設定・有効状態・順序を保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/effect_controls.rs](../../../../crates/ui-egui/src/panels/effect_controls.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>edit.pasteAttributes</code> | <code>{"clips":[id]?,"motion":bool=true,"opacity":bool=true,"timeRemapping":bool=true,"volume":bool=true,"channelVolume":bool=true,"panner":bool=true,"effects":bool&#124;[effectId]=true,"scaleTimes":bool=true}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.removeAttributes</code> | <code>{"clips":[id]?,"motion":bool=true,"opacity":bool=true,"timeRemapping":bool=true,"volume":bool=true,"channelVolume":bool=true,"panner":bool=true,"effects":bool&#124;[effectId]=true}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>effects.apply</code> | <code>{"clips":[id]?,"effect":"gaussian_blur&#124;Gaussian Blur&#124;…"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.list</code> | <code>{"kind":"Video"&#124;"Audio"&#124;"VideoTransition"&#124;"AudioTransition"?,"folder":"Video Transitions/Wipe"?,"detail":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.remove</code> | <code>{"clip":id,"index":n}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.reset</code> | <code>{"clip":id,"index":n}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.resetParam</code> | <code>{"clip":id,"effect":str&#124;index,"param":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.select</code> | <code>{"clip":id,"effect":index&#124;id}&#124;{"none":true}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.setDefaultTransition</code> | <code>{"effect":"constant_power&#124;constant_gain&#124;exponential_fade&#124;&lt;video transition&gt;"}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>effects.setInterpolation</code> | <code>{"clip":id,"effect":str&#124;index,"param":str,"mediaTime":ticks,"interpolation":"linear&#124;bezier&#124;autoBezier&#124;continuousBezier&#124;hold&#124;easeIn&#124;easeOut"}&#124;{"keyframes":[{"clip":id,"effect":index,"param":str,"mask":n?,"time":mediaTicks}],"interpolation":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.setParam</code> | <code>{"clip":id,"effect":"motion"&#124;index,"param":str,"mask":n?,"value":num&#124;[x,y]&#124;"#rrggbb"&#124;bool&#124;path&#124;"option name" (a choice takes its index or its name),"time":ticks? (where the keyframe goes when the parameter is animated, kept there even outside the clip; default: the playhead, pinned to the clip; a parameter that is not animated gets a new static value whatever the time),"keyframe":bool? (true: write a keyframe at `time` and animate the parameter),"merge":bool&#124;key?,"begin":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.toggleAnimation</code> | <code>{"clip":id,"effect":str&#124;index,"param":str,"mask":n?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>effects.toggleEnabled</code> | <code>{"clip":id,"index":n}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。

<a id="premiere-27-12"></a>

## プロパティで映像・音声効果とマスクを調整する（27.0との照合）

簡易カードと詳細パネルは同じ効果・マスクIDを参照する。一方の値、バイパス、キーフレームの変更を他方にも反映し、選択変更時は対象を切り替える。
