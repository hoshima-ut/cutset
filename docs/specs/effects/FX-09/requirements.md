# FX-09 透明度とブレンド — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

積層順・不透明度・ブレンド演算から出力画素とアルファを決める。

## 受入条件

Screen・Multiply・通常の結果を既知の色で比較する。透明画素を含む書き出しを再読込する。

## 例外と復旧

アルファを保存できない納品形式では背景合成の設定を求める。透明領域の色成分が輪郭の縁に混ざらないよう変換する。

## 参照資料と確認項目

- [A457](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/create-fade-in-video-effects.html)　クリップ先頭の透明度を0から100へ変化させ、下層の映像が最初だけ見えるか見る。（公開手順）
- [A494](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-composites/compositing-overview.html)　下段の市松模様へ半透明ロゴを重ね、順序を入れ替えた結果と比較する。（公開手順）
- [A495](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-composites/combine-multiple-videos-or-stil-images-using-blend-modes.html)　二映像の上層へMultiplyを指定し、同じピクセルを通常合成した場合と見比べる。（公開手順）
- [A496](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-composites/blend-mode-options.html)　同じ色票でScreenとMultiplyを切り替え、黒・白・中間色それぞれの表示を照合する。（公開手順）
- [A497](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-composites/specify-clip-opacity.html)　単クリップの不透明度を100、50、0に設定し、下層の映像の透け方を確認する。（公開手順）
