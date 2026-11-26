# ラベル・時刻・注記の要件（IO-17）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材・シーケンスの時刻とマーカーを区別し、ラベルやコメントで探す。

## 受入条件

29.97 DFの分境界、同素材が複数あるシーケンスで、素材マーカーとシーケンス指示の時刻を照合。

## 例外と復旧

同じ時刻表示でも所有者が異なる候補を混在させない。無効なドロップフレーム表記は修正位置を示す。

## 参照資料と確認項目

- [A172](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/label-colors-in-sequence-tabs.html)　用途別の色を付けた複数のシーケンスタブを開き、同名に近い編集版を色と名前の両方で識別できるか確かめる。（公開手順）
