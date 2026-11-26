# AU-04 クリップゲイン — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

絶対値・相対値・ピーク基準で個別または複数配置のゲインを調整する。

## 受入条件

音量の異なる二素材で相対バランスが維持される操作と個別に揃う操作を確認する。

## 例外と復旧

無音区間の正規化では補正量を計算できない旨を表示する。ほかの配置まで無限大の増幅を適用しない。

## 参照資料と確認項目

- [A533](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/adjust-gain-in-audio.html)　強弱の異なる二クリップにピーク正規化の各モードを適用し、相対音量の違いを見る。（公開手順）
