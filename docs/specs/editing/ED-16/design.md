# ED-16 素材の一括配置 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材を選び、選択順またはビンの表示順、連続配置またはマーカー配置を指定して仮の配置表を確認する。

## データと処理境界

開始位置・並び順・素材ごとのIn/Outから配置表を一度作る。選択確定後のビン再ソートで配置表を変更しない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/place_items_tests.rs](../../../../crates/engine/src/place_items_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.automateToSequence</code> | <code>{"items":[id]?,"ordering":"sort&#124;selection"?,"placement":"sequentially&#124;unnumberedMarkers"?,"method":"insert&#124;overwrite"?,"overlapFrames":n=30,"stillFrames":n?,"videoTransition":bool=true,"audioTransition":bool=true,"ignoreAudio":bool=false,"ignoreVideo":bool=false}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
