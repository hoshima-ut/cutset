# ショット検出の開始の要件（MN-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

動画を選び、検出結果をマーカー・サブクリップ・実カットから選ぶ。

## 受入条件

色面を三つ連ねた映像に連続音をリンクする。マーカーのみを選べば音声配置は一つのまま、検出した画の境界に注記が付く。

## 例外と復旧

静止画や解析不能素材では解析を開始しない。解析中止時は未確認の境界を確定しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/detect-edit-points-using-scene-edit-detection.html)
