# 入れ子と簡略版の設計（ED-24）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

範囲を入れ子にして子を開き、親へ戻って反映を確認する。展開や簡略化は新しい版へ適用する。

## データと処理境界

親は子シーケンスIDと参照範囲を保存する。展開時は親時刻へ変換し、元の子と新しい配置の対応を記録する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/nest_fidelity_tests.rs](../../../../crates/engine/src/nest_fidelity_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.nest</code> | <code>{"name":str?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.makeSubsequence</code> | <code>{"name":str?}</code> | [sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs) |
| <code>sequence.nestSequences</code> | <code>{"on":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>sequence.revealNested</code> | <code>{}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
