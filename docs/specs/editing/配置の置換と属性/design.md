# 配置の置換と属性の設計（ED-21）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象配置と置換元を選び、素材先頭または照合フレームを基準に合わせる。保持する効果・音声・属性を確定する。

## データと処理境界

宛先の時間範囲、選択属性、置換元の素材IDと素材点をまとめて渡し、影響する配置を返す。無効化は配置を残したまま出力状態を変える。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/clip_ops.rs](../../../../crates/engine/src/clip_ops.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.replaceFromBin</code> | <code>{"clips":[id]?,"item":id?,"keepSourceIn":bool=false}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.replaceFromSource</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.replaceFromSourceMatchFrame</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
