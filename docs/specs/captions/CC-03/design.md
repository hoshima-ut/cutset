# CC-03 外部字幕と翻訳 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

外部字幕の言語・時刻基準と読み込み先を確認し、新規または既存トラックを選ぶ。翻訳候補は別言語のトラックに生成して校正する。

## データと処理境界

入力時刻をシーケンスの時間単位へ正規化し、本文、改行、元の識別子・利用可能な設定を保持する。翻訳結果は原文字幕IDを参照しつつ別の本文を持つ。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/captions.rs](../../../../crates/engine/src/captions.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>captions.export</code> | <code>{"path":str,"format":"srt&#124;vtt&#124;scc&#124;mcc&#124;stl&#124;ttml&#124;dfxp"? (default: from the extension),"track":id&#124;"C1"?,"dropFrame":bool=true}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |
| <code>captions.import</code> | <code>{"path":str,"name":str?,"language":str?}</code> | [captions.rs](../../../../crates/engine/src/captions.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
