# FX-20 時間効果 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

速度キー、逆再生、停止とフレーム補間で画を時間方向に変換する。

## 受入条件

ソースのフレーム番号を焼いた素材で、前進→停止→逆行の順序を照合する。

## 例外と復旧

計算された素材時刻が範囲外に出る場合は不足する端を表示する。補間が使えない経路では選べるサンプリング方法を示す。

## 参照資料と確認項目

- [A424](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/time-effects.html)　フレーム番号入り動画を低い更新頻度へ間引き、元の尺を維持して番号が繰り返される箇所を見る。（公開手順）
- [A431](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/adjust-effect-speed.html)　二つの位置キーの間隔を半分にして、同じ移動距離を短い時間で通るか再生する。（公開手順）
