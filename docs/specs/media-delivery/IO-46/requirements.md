# IO-46 字幕と文字データ — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

字幕の焼き込み・別ファイル・埋込みと文字起こしの出力先を指定する。

## 受入条件

日本語の改行、開始時刻、字幕トラックの言語・表示の有無を確認。埋め込み非対応の組で、生成される成果物が明確か試す。

## 例外と復旧

非対応のスタイルや埋込みは失われる項目を列挙する。サイドカーへの切替は編集者が選ぶ。

## 参照資料と確認項目

- [A642](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-transcripts.html)　話者を区別した文字起こしを出力し、発言順・話者・時刻が選んだ形式でどこまで残るか読む。（公開手順）
- [A643](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-caption-tracks.html)　2言語のうち指定した字幕トラックを出力し、字幕本文・改行・開始時刻をファイルで照合する。（公開手順）
- [A644](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-captions.html)　離れた二つの字幕を選択して書き出し、未選択の字幕が紛れ込まないか確認する。（公開手順）
- [A645](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-text-from-motion-graphics.html)　グラフィックスに異なる社名を入れ、出力された文字列で両方の表記を校正できるか試す。（公開手順）
