# 文字起こしから字幕の設計（CC-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

話者付きの文字起こしを時刻とともに校正し、表示文字数・行数・目安尺を指定する。生成案を確認して新しい字幕トラックを作成する。

## データと処理境界

発話の素材時刻を配置のシーケンス時刻へ写像し、決定した字幕区間と本文を保存する。生成後の字幕編集は元の認識語・映像編集から独立させる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/captions.rs](../../../../crates/engine/src/captions.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>transcript.createCaptions</code> | <code>{"maxChars":n?,"lines":1&#124;2?,"minSeconds":f?,"maxSeconds":f?,"gapFrames":n?,"format":str?,"name":str?}</code> | [transcript.rs](../../../../crates/engine/src/transcript.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
