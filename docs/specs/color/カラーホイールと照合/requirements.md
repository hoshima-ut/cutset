# カラーホイールと照合の要件（CO-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

明・中・暗部の色を調整し、基準ショットとの一致を画とスコープで比べる。

## 受入条件

参照ショットの変更前後と、適用先以外が不変であることを確認する。

## 例外と復旧

基準フレームがオフライン、または調整先がロック済みなら適用を保留する。再選択しても未採用案を適用しない。

## 参照資料と確認項目

- [A585](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/correct-color-using-color-wheel.html)　シャドウ・中間調・ハイライトの各ホイールを動かし、階調ごとの変化を確認する。（公開手順）
- [A586](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/match-color-between-shots.html)　別カメラの二ショットで参照フレームを設定し、照合後に顔と背景を比較する。（公開手順）
