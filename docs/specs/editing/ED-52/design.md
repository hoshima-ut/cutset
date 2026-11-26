# ED-52 モニターの範囲と挿入 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材側でI/Oを決め、映像のみ・音声のみ・両方を選び、完成側の宛先でボタンまたは割当キーから挿入する。

## データと処理境界

操作は焦点のモニター、素材範囲、パッチ先と編集モードを明示してエンジンへ送る。完成側のIn/Outと素材側のIn/Outを独立させる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.matchFrame</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.reverseMatchFrame</code> | <code>{}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
