# ガイドの編集の要件（MN-23）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

向き、位置、単位、色を選んで表示ガイドを追加・固定・消去する。

## 受入条件

ロック中のガイドはドラッグしても座標を保つ。解除して移動すると指定単位で位置が変わり、出力画像にはガイドが載らない。

## 例外と復旧

範囲外の値や不正な単位は修正を促す。固定済みの線にドラッグしても値を更新しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/add-or-remove-guides.html)
