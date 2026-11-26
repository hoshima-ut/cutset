# 基本補正の設計（CO-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

中立のパッチを採取して白点を設定し、露光と彩度を調整する。自動値を提案した後でも各項目を数値で変更できる。

## データと処理境界

白点・露光・コントラスト・階調・彩度を独立したパラメーターに保持し、自動補正も同じ項目に値を設定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/color.rs](../../../../crates/engine/src/color.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>lumetri.applyMatch</code> | <code>{"clip":id?,"referenceTime":ticks?&#124;"referenceFrame":n?&#124;"referenceTimecode":str?,"faceDetection":bool=true}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.applyPreset</code> | <code>{"name":str,"clips":[id]?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.exportCube</code> | <code>{"clip":id?,"path":str,"size":n=33}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.presetThumbnails</code> | <code>{"folder":str?,"names":[str]?,"width":n=160,"columns":n=4,"path":str?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.presets</code> | <code>{"folder":str?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.setInputLut</code> | <code>{"clip":id?,"lut":"lib:&lt;id&gt;"&#124;"builtin:&lt;id&gt;"&#124;""?,"path":str?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.setLook</code> | <code>{"clip":id?,"lut":"lib:&lt;id&gt;"&#124;"builtin:&lt;id&gt;"&#124;""?,"path":str?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lumetri.setSection</code> | <code>{"clip":id?,"section":"basic"&#124;"creative"&#124;"curves"&#124;"wheels"&#124;"hsl"&#124;"vignette","on":bool?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
