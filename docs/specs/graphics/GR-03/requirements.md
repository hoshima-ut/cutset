# GR-03 レイアウト追従 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

基準レイヤーと端に対する固定位置、尺変更時に保持するアニメ区間を指定する。

## 受入条件

テロップ文字を長くし、クリップ尺を伸縮しても帯と文字の関係、入退場の速さを確認できる。

## 例外と復旧

ピンの循環や保護区間の合計より短い尺は確定前に検出し、参照先または尺を修正できる。

## 参照資料と確認項目

- [A344](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/create-responsive-graphics.html)　帯を名前テキストに固定し、短い姓から長い姓名に変えたときの余白を見る。（公開手順）
- [A345](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/preserve-intro-outro-animations-while-creating-responsive-design-graphics.html)　冒頭と末尾の動きを保護してクリップを延ばし、入退場のフレーム数を変更前と比べる。（公開手順）
