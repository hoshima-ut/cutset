# 素材からの範囲選択の要件（ED-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材のIn/Outを決めて、映像、音声、または両方を取り出す。

## 受入条件

素材を試聴してもシーケンス上の絵が置換されない。片方だけをドラッグすると指定した要素のみ入る。

## 例外と復旧

音声なし素材の音声のみ操作は無効にし、宛先トラックや現在の選択を変更しない。

## 参照資料と確認項目

- [A103](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/set-in-and-out-points-in-the-source-monitor.html)　開始・終了点を同じ素材に打ち、表示された選択尺と実際に挿入されたフレーム数が一致するか確認する。（公開手順）
