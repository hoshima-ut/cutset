# 配置表の点検の要件（ED-54）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

列の並べ替えと条件で異常候補を探し、該当フレームを開いて確認する。

## 受入条件

オフライン1件と意図した一瞬のカットを含む案件で、行・タイムライン・CSVを対応付ける。

## 例外と復旧

絞り込み中に配置が移動・削除された場合、旧時刻の別配置にジャンプせず行を更新する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/navigate-timelines-with-sequence-index.html)
