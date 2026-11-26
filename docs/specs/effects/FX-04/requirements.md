# FX-04 調整レイヤー — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

上のレイヤーが覆う時空間の下位トラックに一組の処理を適用する。

## 受入条件

調整レイヤーの尺の内外、上下のトラック、非表示時を比較する。

## 例外と復旧

入力が透明だけの時刻は透明を維持する。調整レイヤーの無効化で下位素材や個別効果を書き換えない。

## 参照資料と確認項目

- [A403](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/create-adjustment-layers.html)　二つのカットの上に調整レイヤーを置き、重なる部分だけに共通の色補正が出るか確認する。（公開手順）
- [A404](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/resize-adjustment-layers.html)　調整レイヤーの空間寸法を縮小し、画面の内外で下層へ掛かる処理範囲を見比べる。（公開手順）
