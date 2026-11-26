# 映像トランジションの設計（FX-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

編集点を選び、切替方式・尺・揃え方を指定する。両側のハンドルと時間軸に表示される実際の遷移区間を確認して確定する。

## データと処理境界

隣接配置の端、素材側の余長、揃え方から必要なサンプル範囲を計算する。端の反復を選んだ場合は実フレーム利用部分と区別する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/transition_controls.rs](../../../../crates/ui-egui/src/panels/transition_controls.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.applyVideoTransition</code> | <code>{"clip":id?,"effect":"cross_dissolve&#124;Cross Dissolve&#124;…"?,"frames":i64?,"edge":"in"&#124;"out"?,"align":"center"&#124;"start"&#124;"end"?,"params":{param:value}?,"reverse":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.removeTransition</code> | <code>{"transitions":[id]?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.setTransition</code> | <code>{"transition":id,"params":{param:value}?,"reverse":bool?,"reset":bool?,"duration":ticks?&#124;"frames":n?,"align":"center"&#124;"start"&#124;"end"?&#124;"start":ticks?,"merge":bool?,"begin":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
