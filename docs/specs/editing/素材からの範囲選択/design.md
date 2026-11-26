# 素材からの範囲選択の設計（ED-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材モニターで開始・終了を指定し、映像、音声、両方のどれを挿入するか選ぶ。

## データと処理境界

素材IDと素材時間の範囲、選択したストリームを入力とする。タイムライン上の配置が作られるのはドロップまたは挿入が確定した時点。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>source.close</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>source.closeAll</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>source.inspect</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>source.open</code> | <code>{"item":id?,"clip":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>source.setPlayhead</code> | <code>{"time":ticks&#124;"frame":i64&#124;"seconds":f64}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
