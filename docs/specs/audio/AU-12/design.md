# AU-12 音声フェード — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

音声の編集点または端を選び、フェード長と曲線を指定する。中点をループ試聴し、片側のフェードとクロスフェードを区別して表示する。

## データと処理境界

サンプル時刻に対する各入力のゲインを計算する。線形クロスフェードでは対応ゲインの和、等パワーではゲインの二乗和が一定となる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/transition_controls.rs](../../../../crates/ui-egui/src/panels/transition_controls.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.applyAudioTransition</code> | <code>{"clip":id?,"effect":"constant_power&#124;Constant Power&#124;…"?,"frames":i64?,"edge":"in"&#124;"out"?,"align":"center"&#124;"start"&#124;"end"?,"params":{param:value}?,"reverse":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
