# MN-35 パネル別の操作検索 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

選択対象とパネルで有効な操作、無効理由、同じ操作を起動するキーを示す。

## 受入条件

選択なし、単一、複数、不均一な種類の選択で比較。複数選択時に一項目だけへ誤適用されないか確認。

## 例外と復旧

選択が変わって条件を満たさなくなった命令は理由を表示して中止する。混在選択の先頭だけへ暗黙に実行しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/display-panel-options-and-menu.html)
