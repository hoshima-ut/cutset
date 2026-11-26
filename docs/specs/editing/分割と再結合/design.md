# 分割と再結合の設計（ED-19）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

再生ヘッドを配置の内側に置いて分割し、隣接した2配置を選んで素材が連続する境界を再結合する。

## データと処理境界

分割点で左右の素材範囲を相補的に作る。結合時は原本、素材境界、速度、対応する属性を照合する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/clip_ops.rs](../../../../crates/engine/src/clip_ops.rs)、[crates/edit/src/lib.rs](../../../../crates/edit/src/lib.rs)。

確認した関数：[razor](../../../../crates/edit/src/lib.rs)。指定トラック上の内部境界で配置を分割し、ロックされたトラックを除外して新しい配置IDを返す。分割点を跨ぐ素材時刻の連続性に既存試験がある。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.addEdit</code> | <code>{"time":ticks?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.addEditAllTracks</code> | <code>{"time":ticks?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.joinThroughEdits</code> | <code>{"clips":[id]?,"cut":[id,id]?,"all":bool?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>timeline.razor</code> | <code>{"time":ticks,"track":"V1"&#124;id?,"clip":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
