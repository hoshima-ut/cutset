# IO-01 案件とテンプレート — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

新規作成で保存先を決め、ひな型のビンと初期シーケンスを確認して作成する。成功後は作成した案件を開く。

## データと処理境界

ひな型から案件内の参照関係を複製し、新規案件と保存先に独立した識別子を割り当てる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_tools.rs](../../../../crates/engine/src/project_tools.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.newProject</code> | <code>{"name":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newProjectFromTemplate</code> | <code>{"template":name&#124;path,"name":str?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
