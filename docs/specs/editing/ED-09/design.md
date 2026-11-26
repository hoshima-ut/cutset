# ED-09 シーケンス作成 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

新規シーケンスでプリセットまたは基準素材を選び、寸法・レート・音声設定を確認して作成する。

## データと処理境界

シーケンスの有理数レート、フレーム寸法、画素比、音声サンプルレートを明示して保存し、各素材の解釈を別に保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.newSequence</code> | <code>{"name":str,"width":u32=1920,"height":u32=1080,"fps":f64=23.976,"sampleRate":u32=48000,"video":n=3,"audio":n=3,"mix":"Stereo&#124;Mono&#124;5.1&#124;Adaptive"?,"trackType":"Standard&#124;Mono&#124;5.1&#124;Adaptive"?,"fromItem":itemId?,"fromItems":[itemId]?,"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newSequenceFromClip</code> | <code>{"items":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
