# IO-10 素材の解釈 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

変更元の素材と使用中の配置を確認し、レート、画素比、フィールド順等を個別に上書きする。

## データと処理境界

検出値と上書き値を別々に保つ。新しいフレームレートで素材時刻を解釈し、配置が参照できる尺を再評価する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/par_tests.rs](../../../../crates/engine/src/par_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.fieldOptions</code> | <code>{"clips":[id]?,"reverseFieldDominance":bool=false,"processing":"none&#124;alwaysDeinterlace&#124;flickerRemoval"?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.interpretFootage</code> | <code>{"items":[id]?,"colorSpace":"auto"&#124;"&lt;color space id&gt;"?,"pixelAspect":[num,den]&#124;"file"?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>clip.modifyTimecode</code> | <code>{"item":id?,"timecode":"HH:MM:SS:FF"?,"frame":i64?,"tapeName":str?,"reset":bool?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
