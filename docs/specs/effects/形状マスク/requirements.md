# 形状マスクの要件（FX-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

矩形、楕円、自由曲線で領域を作り、反転・フェザー・拡張を調整する。

## 受入条件

同じ輪郭で「領域だけぼかす」と「領域だけ見せる」の結果を別々に確認する。

## 例外と復旧

面積ゼロの輪郭は警告し、頂点編集へ戻れる。クリップを切り替えても別効果のマスクを変更しない。

## 参照資料と確認項目

- [A367](https://helpx.adobe.com/premiere/desktop/add-text-images/draw-objects/create-free-form-shapes-for-masking.html)　複雑な輪郭を閉じた自由形状で囲み、最後の点と最初の点の間に隙間が残らないか確認する。（26.0で矩形・楕円・ペンのマスクツールを刷新）
- [A448](https://helpx.adobe.com/premiere/desktop/add-video-effects/create-masks-and-composites/create-masks-using-shapes.html)　映像の一部分を囲ったぼかしマスクを作り、内側と外側の境目を同じフレームで見比べる。（公開手順）
- [A449](https://helpx.adobe.com/premiere/desktop/add-video-effects/create-masks-and-composites/create-reveal-animations-using-masking-techniques.html)　マスク位置に始終のキーを置き、文字が徐々に見える過程と最終画を確認する。（公開手順）
- [A481](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/rectangle-ellipse-and-pen-masks.html)　矩形・楕円・ペンで同じ被写体を囲み、角や曲線のハンドル操作で直せる範囲を比較する。（26.0で矩形・楕円・ペンのマスクツールを刷新）
- [A483](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/create-masks-using-shapes.html)　楕円マスクの中心と大きさを変え、被写体の目だけがぼかし範囲に入るよう調整する。（26.0で矩形・楕円・ペンのマスクツールを刷新）
- [A487](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/adjust-mask-properties.html)　フェザー・拡張・反転を一項目ずつ変え、境界の位置と柔らかさを区別して確認する。（公開手順）
- [A491](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/modifiers-and-conditions-for-masking.html)　マスクの点を通常ドラッグと修飾キー付きで動かし、方向の制約やハンドルの変化を確認する。（公開手順）
