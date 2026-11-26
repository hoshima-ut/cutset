# CC-01 文字起こしから字幕 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

話者と時刻を持つ文字列を校正し、長さ・改行・表示時間に基づいて字幕に分ける。

## 受入条件

字幕生成前の本文修正と生成後の個別字幕修正を分け、元の発話・映像の尺を照合する。

## 例外と復旧

単語時刻欠落や早口で制約を同時に満たせない区間には再分割候補を表示する。確定済み字幕を再生成する際は出力先を明示する。

## 参照資料と確認項目

- [A370](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/about-captions.html)　字幕トラックの表示を切り替え、画面文字との違いと字幕時刻の位置を確認する。（公開手順）
- [A371](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/auto-transcribe-video-using-speech-to-text.html)　二話者の日本語音声を指定して書き起こし、発話開始と固有名詞の聞き誤りを原音と照合する。（26.2で話者判定等、26.5で発声検出モデルを改善）
