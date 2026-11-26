# ED-28 ロールトリム — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

隣接する前後2配置の共通境界を指し、両側の絵を見ながら編集点を動かす。

## データと処理境界

前配置の末尾と後配置の先頭に同じ時刻差を適用し、外側2端を固定する。両側で成立する素材余白の共通範囲を求める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/trim.rs](../../../../crates/engine/src/trim.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>timeline.roll</code> | <code>{"left":id,"right":id,"delta":ticks&#124;"deltaFrames":i64,"followLinks"?:bool}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
