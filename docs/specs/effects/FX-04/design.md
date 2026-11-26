# FX-04 調整レイヤー — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

調整レイヤーを上位トラックへ置き、開始・終了と効果を指定する。トラック出力を一時的に切って効果の対象を比較する。

## データと処理境界

対象時刻で下位トラックを合成した画像をレイヤーの入力とする。配置の有効区間を半開区間で評価し、上位の素材は後から合成する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/render/src/plan.rs](../../../../crates/render/src/plan.rs)。

確認した関数：[adjustment_ops](../../../../crates/render/src/plan.rs)。調整レイヤーの効果処理をレンダー計画に組み込み、端末能力を判定する。パネル操作と保存再開後の一致は別試験になる。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.newAdjustmentLayer</code> | <code>{"seconds":f64=5,"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
