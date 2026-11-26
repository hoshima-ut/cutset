# GR-02 図形・画像レイヤー — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

パス、形状、画像、映像を重ね、順序・グループ・グラデーションを指定する。

## 受入条件

半透明ロゴ・見出し・帯を別々に編集し、グループ移動後も相対位置が合う。

## 例外と復旧

親を子の下へ移すなど循環するグループ化は拒否する。オフライン画像があっても図形と他レイヤーの位置を保持する。

## 参照資料と確認項目

- [A346](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/group-text-and-graphic-layers.html)　ロゴと文字をグループにして移動し、解除後は文字だけを動かせるか試す。（公開手順）
- [A347](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/create-a-clip-layer.html)　動画をグラフィック内のレイヤーに加え、枠内で再生しながら上のタイトルが読み続けられるか確認する。（公開手順）
- [A349](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/add-gradients.html)　図形に異なる二色のグラデーションを設定し、向きを反転して色の位置を見比べる。（公開手順）
- [A352](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/rename-layers.html)　同じ形の二レイヤーの一方を改名し、再開後に名前で正しい方を選べるか確認する。（公開手順）
- [A359](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/different-ways-to-work-with-graphics.html)　手描きの図形付きタイトルとテンプレート由来のタイトルを選び、編集できるレイヤーの違いを記録する。（公開手順）
- [A362](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/create-markers-in-the-effect-controls-panel.html)　Effect Controlsの特定時刻にマーカーを置き、動きの開始キーとのフレーム差を照合する。（公開手順）
- [A363](https://helpx.adobe.com/premiere/desktop/add-text-images/draw-objects/draw-with-pen-tool.html)　ペンで直線点と曲線点を交互に作り、次の点を追加する前後でハンドルの働きを確認する。（公開手順）
- [A364](https://helpx.adobe.com/premiere/desktop/add-text-images/draw-objects/draw-a-straight-line.html)　三点をクリックして折れ線を描き、点間に意図しない曲率がないか拡大する。（公開手順）
- [A365](https://helpx.adobe.com/premiere/desktop/add-text-images/draw-objects/draw-a-curve.html)　アンカーポイントからハンドルを引いて弧を作り、接線を動かして曲率が変わるか見る。（公開手順）
- [A366](https://helpx.adobe.com/premiere/desktop/add-text-images/draw-objects/create-a-shape.html)　長方形と楕円を別レイヤーに作り、それぞれ独立に塗りと寸法を変更する。（公開手順）
- [A368](https://helpx.adobe.com/premiere/desktop/add-text-images/align-and-distribute-objects/align-objects.html)　高さの異なる三つのロゴを指定基準に揃え、中心または輪郭の一致をガイドで確認する。（公開手順）
- [A369](https://helpx.adobe.com/premiere/desktop/add-text-images/align-and-distribute-objects/distribute-objects.html)　幅の違う三要素を水平方向へ分布させ、設定した基準に対する間隔を測る。（公開手順）
