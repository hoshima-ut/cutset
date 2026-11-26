# CC-02 字幕の手編集 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

区間を追加・分割・統合し、本文、開始終了、位置、スタイルを調整する。

## 受入条件

境界で隣の字幕が重ならず、分割で文言が重複しない。日本語の語分割と読みやすさも確認する。

## 例外と復旧

開始と同じ位置や終了端での分割、ロック中の字幕、隣の字幕をまたぐトリムは理由を示して元の字幕を維持する。

## 参照資料と確認項目

- [A373](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/create-captions.html)　指定の最大文字数・行数で字幕を生成し、長い一文の分割位置と表示区間を読む。（公開手順）
- [A374](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/create-styles-for-captions.html)　新しい字幕スタイルをトラック全体に指定し、二つの離れた字幕で書体と縁の一致を確認する。（公開手順）
- [A375](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/create-single-word-captions.html)　同じ発話から一語表示の字幕を作り、一時停止した各区間で一語ずつ見えるか照合する。（26.3で1語ずつ表示する字幕を追加）
