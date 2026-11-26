# 除去とギャップの設計（ED-20）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

クリップまたはシーケンス範囲を選び、Liftで空白を残すかExtractで後続を詰めるか選ぶ。

## データと処理境界

削除範囲を半開区間で統合し、同時に選んだ重複範囲を一度だけ差し引く。同期対象の後続だけを同じ差分で移動する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/ripple_delete_tests.rs](../../../../crates/engine/src/ripple_delete_tests.rs)、[crates/edit/src/lib.rs](../../../../crates/edit/src/lib.rs)。

確認した関数：[extract](../../../../crates/edit/src/lib.rs)。指定区間の抽出と後続詰めがあり、Liftとの挙動の違いを編集ライブラリで試験する。編集前に影響する字幕や保護行を明示する部分はGUIで別途照合する。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>edit.clear</code> | <code>{"clips":[id]?,"clip":id?} (explicit clips work without a selection)</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.cut</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.rippleDelete</code> | <code>{"clips":[id]?,"clip":id?} (explicit clips work without a selection)</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>edit.rippleDeleteHead</code> | <code>{"clips":[id]?,"clip":id?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.closeGap</code> | <code>{"track":"V1"&#124;id?,"time":ticks?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.extract</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.lift</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>timeline.delete</code> | <code>{"clips":[id]?,"clip":id?,"ripple":bool?} (deletes the named clips, else the selection; ripple closes the gap)</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
