# FX-18 旧効果の読み戻し — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

旧案件を開くと未解決の効果と適用配置を一覧表示する。代替効果を試して対応値を確認し、移行する項目を選ぶ。

## データと処理境界

元の効果ID、バージョン、値、キー、不明フィールドを保持する。移行処理は版ごとの値変換結果と変換できなかった項目を返す。

## 既存実装との対応

方針は「上流対応を要確認」。対象マイルストーンは[M5](../../../development/milestones.md)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>presets.apply</code> | <code>{"preset":str,"clips":[id]?}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.delete</code> | <code>{"name":str}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.export</code> | <code>{"path":str,"names":[str]?}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.import</code> | <code>{"path":str}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.list</code> | <code>{}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.rename</code> | <code>{"name":str,"to":str}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.save</code> | <code>{"clip":id?,"effects":[index]?,"name":str,"description":str?,"keyframes":"scale"&#124;"anchorIn"&#124;"anchorOut"&#124;"none"?}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |
| <code>presets.scan</code> | <code>{}</code> | [presets.rs](../../../../crates/engine/src/presets.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
