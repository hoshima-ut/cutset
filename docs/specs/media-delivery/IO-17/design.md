# IO-17 ラベル・時刻・注記 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材またはシーケンスを選び、その時間軸にラベル・マーカー・注記を追加する。検索結果から対応位置へ移動する。

## データと処理境界

マーカーは所有者IDと内部時刻で保存し、表示上のDF/NDFや素材開始時刻は表示変換時に適用する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/timecode.rs](../../../../crates/ui-egui/src/panels/timecode.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>colors.addCustom</code> | <code>{"color":hex,"name":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>colors.removeCustom</code> | <code>{"color":hex}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>colors.updateCustom</code> | <code>{"color":hex,"replacement":hex?,"name":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.label</code> | <code>{"label":"preset&#124;#RRGGBB","clips":[id]?,"items":[id]?,"sequence":id?,"saveColor":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.label.blue</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.brown</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.caribbean</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.cerulean</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.forest</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.green</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.iris</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.lavender</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.magenta</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.mango</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.purple</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.rose</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.tan</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.teal</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.violet</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.label.yellow</code> | <code>{"items":[id]?,"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>edit.selectLabelGroup</code> | <code>{}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>labels.deletePreset</code> | <code>{"name":str}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |
| <code>labels.exportPreset</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |
| <code>labels.importPreset</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |
| <code>labels.presets</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
