# カット点検出の要件（ED-25）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

一本化した映像から切れ目を提案し、点・範囲・分割のいずれかを選ぶ。

## 受入条件

既知の3カットとフラッシュを含む素材で正検出・見逃し・誤検出、誤検出の修正時間を記録する。

## 例外と復旧

デコード失敗の区間は未解析として明示する。解析中止や未確定候補の操作で実カットを増やさない。

## 参照資料と確認項目

- [A274](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/detect-edit-points-using-scene-edit-detection.html)　既知の編集済み映像を分析し、検出点をマーカー・実カット・サブクリップに出した結果とリンク音声への作用を比較する。（既存機能。Windows RTXの追加高速化は27.0）
