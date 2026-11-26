# AU-05 配置のミキシング — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

再生ヘッド下の対象配置を確認してフェーダーとパンを操作する。書込モードではタッチ開始・終了を記録し、通常時は設定値を調整する。

## データと処理境界

配置キーは配置ローカル時刻で保持する。トラックフェーダーと配置ゲインの評価段を分け、配置移動後も調整が同じ素材部分に対応する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/mixer.rs](../../../../crates/engine/src/mixer.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clipMixer.release</code> | <code>{"track":"A1"&#124;id,"lane":"volume&#124;pan","time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>clipMixer.set</code> | <code>{"clip":id,"effect":"volume"&#124;"panner","param":"level"&#124;"balance","value":f64,"keyframe":bool?,"time":ticks?,"begin":bool?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>clipMixer.setMode</code> | <code>{"track":"A1"&#124;id,"mode":"Off&#124;Read&#124;Latch&#124;Touch&#124;Write"}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |
| <code>clipMixer.touch</code> | <code>{"track":"A1"&#124;id,"lane":"volume&#124;pan","value":f64,"time":ticks?}</code> | [mixer.rs](../../../../crates/engine/src/mixer.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
