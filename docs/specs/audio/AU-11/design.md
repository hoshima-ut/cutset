# AU-11 音楽の尺合わせ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

目標尺と優先する冒頭・終端範囲を指定し、提案された接続点を順に試聴する。採用後は元構成との切替と再調整を可能にする。

## データと処理境界

再生順に並べた元素材の区間列とクロスフェードを持ち、曲のテンポを維持する。実現尺と目標尺の差をサンプルまたは時間で返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/remix.rs](../../../../crates/engine/src/remix.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.remix</code> | <code>{"clip":id?,"duration":ticks?,"seconds":f64?,"frame":n?,"timecode":str?,"segments":0..100?,"variations":0..100?}</code> | [remix.rs](../../../../crates/engine/src/remix.rs) |
| <code>clip.remix.enable</code> | <code>{"clip":id?}</code> | [remix.rs](../../../../crates/engine/src/remix.rs) |
| <code>clip.remix.properties</code> | <code>{"clip":id?,"duration":ticks?,"seconds":f64?,"frame":n?,"timecode":str?,"segments":0..100?,"variations":0..100?}</code> | [remix.rs](../../../../crates/engine/src/remix.rs) |
| <code>clip.remix.revert</code> | <code>{"clip":id?}</code> | [remix.rs](../../../../crates/engine/src/remix.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
