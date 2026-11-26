# 配置のミキシングの要件（AU-05）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

再生位置にある配置のレベルとパンを操作し、必要に応じてキーを書く。

## 受入条件

一つの配置を移動させ、クリップ側の調整が付いて動くことを確認する。

## 例外と復旧

ヘッドが隙間にある、対象が曖昧、配置がロックされている場合は対象を示して書込みを保留する。

## 参照資料と確認項目

- [A550](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/set-automation-modes-for-audio-clip-mixer.html)　Audio Clip Mixerでキー書き込みを切り替え、再生中に動かした値がクリップに記録されるか見る。（公開手順）
