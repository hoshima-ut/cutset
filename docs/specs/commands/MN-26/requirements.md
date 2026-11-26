# MN-26 一覧パネルへの移動 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

配置表とマーカー一覧を開き、行から対応する再生位置に移動する。

## 受入条件

一フレームの空白を一覧から選ぶとその時刻を開く。マーカーの色フィルターを戻すと非表示だった注記が同じ数だけ現れる。

## 例外と復旧

一覧表示後に空白が埋まった場合は再読込し、同じ行番号の別カットにジャンプしない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/navigate-timelines-with-sequence-index.html)
