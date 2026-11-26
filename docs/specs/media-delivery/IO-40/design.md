# IO-40 納品範囲 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

出力元と範囲を選び、先頭・末尾の画と総フレーム数を確認してからジョブを確定する。

## データと処理境界

UIのIn/Outを内部の半開範囲へ変換し、出力元ID、版、実効範囲をジョブに保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/export_mode/preview.rs](../../../../crates/ui-egui/src/panels/export_mode/preview.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportAle</code> | <code>{"path":str,"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>file.exportInterchange</code> | <code>{"format":"edl&#124;xml&#124;fcpxml&#124;otio&#124;aaf&#124;omf"=xml,"path":str,"sequence":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.exportMedia</code> | <code>{"path":str,"preset":str?,"settings":ExportSettings?,"format":"h264&#124;hevc&#124;prores&#124;dnxhr&#124;apv&#124;mjpeg&#124;mxf-op1a&#124;mxf-opatom&#124;png&#124;tiff&#124;bmp&#124;jpg&#124;tga&#124;dpx&#124;exr&#124;gif&#124;wav&#124;aiff&#124;aac&#124;mp3&#124;flac"?,"audioCodec":"auto&#124;aac&#124;pcm&#124;flac"?,"flacLevel":0..8=5,"width":u32?,"height":u32?,"fps":f64?,"bitrateKbps":u32?,"bitrateMode":"cbr&#124;vbr1Pass&#124;vbr2Pass&#124;crf"?,"crf":0..51=23,"hardwareEncoding":"off&#124;auto"?,"scale":f32=1,"audio":bool=true,"quality":0..100,"burnCaptions":bool=false,"alpha":bool=false,"exrCompression":"none&#124;rle&#124;zips&#124;zip"?,"captionSidecar":"srt&#124;vtt"?,"loudnessLufs":f64?,"proresProfile":"proxy&#124;lt&#124;standard&#124;hq&#124;4444&#124;4444xq"?,"dnxProfile":"lb&#124;sq&#124;hq&#124;hqx"?,"apvProfile":"422-10&#124;422-12&#124;444-10&#124;444-12&#124;4444-10&#124;4444-12&#124;400-10"?,"h264Profile":"baseline&#124;main&#124;high&#124;high10"?,"h264IntraOnly":bool=false,"mxfVideoCodec":"dnxhr&#124;proRes&#124;h264"?,"sequence":id?,"range":"entire&#124;inOut&#124;workArea&#124;custom"?,"startSeconds":f64?,"endSeconds":f64?,"wait":bool=false}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.exportSelectionProject</code> | <code>{"path":str,"items":[id]?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
