# 素材の収集と保管の設計（IO-56）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

必要なシーケンスを選び、依存素材と容量、コピー・変換の方法を確認して収集する。

## データと処理境界

収集対象にはネスト、使用中の代理・フォント・拡張等の外部依存を含めて分類する。新しい案件を同梱素材へ参照し直す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_manager.rs](../../../../crates/engine/src/project_manager.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.projectManager</code> | <code>{"destination":str,"mode":"collect&#124;consolidate","sequences":[id]?,"excludeUnused":bool=true,"handles":frames=30,"preset":"prores_lt&#124;prores_hq&#124;h264&#124;…","includeProxies":bool,"includePreviews":bool=false,"projectName":str?,"dryRun":bool=false,"overwrite":bool=false,"wait":bool=false}</code> | [project_manager.rs](../../../../crates/engine/src/project_manager.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
