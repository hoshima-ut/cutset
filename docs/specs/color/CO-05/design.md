# CO-05 ルックとLUT — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

LUTを登録し、入力変換用かクリエイティブルック用かを指定する。強度を変えてプレビューした後に案件へ関連付ける。

## データと処理境界

LUTの入力・出力空間と内容識別値を記録する。ルックの強度は補正前後の混合比として扱い、媒体の入力解釈とは個別に設定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/color.rs](../../../../crates/engine/src/color.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>lut.export</code> | <code>{"lut":"lib:&lt;id&gt;"&#124;"builtin:&lt;id&gt;","path":str,"format":"cube"&#124;"3dl"?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lut.import</code> | <code>{"path":str,"name":str?}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lut.list</code> | <code>{}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>lut.remove</code> | <code>{"id":str}</code> | [color.rs](../../../../crates/engine/src/color.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
