# ED-26 端のトリム — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

前端または後端を選び、伸縮後の最終フレームを試聴してドラッグを確定する。

## データと処理境界

素材端・隣接配置・最短尺から許容差分を計算し、要求値と実際の差分を表示する。通常トリムは他配置の時刻を保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/trim.rs](../../../../crates/engine/src/trim.rs)、[crates/edit/src/lib.rs](../../../../crates/edit/src/lib.rs)。

確認した関数：[trim](../../../../crates/edit/src/lib.rs)。配置のロックと素材余白・隣接配置を調べ、許容範囲に収めた実差分を返す。既存試験の制約を画面上のプレビューと確定結果でも一致させる。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>timeline.trim</code> | <code>{"clip":id,"edge":"in&#124;out","mode":"regular&#124;ripple","delta":ticks&#124;"deltaFrames":i64,"linked":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
