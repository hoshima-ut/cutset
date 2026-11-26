# ED-20 除去とギャップ — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

選んだ配置や範囲を消し、ギャップ維持または後続詰めを選ぶ。

## 受入条件

中央12フレームをLiftすると空白、Extractすると後続は12フレーム前。無関係なロック領域を維持する。

## 例外と復旧

範囲が空なら変更せず、保護した行と衝突する要求は適用前に一覧にする。

## 参照資料と確認項目

- [A264](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/lift-and-paste-frames.html)　範囲をLiftして残ったギャップと、別位置に貼り付けたフレームの尺・順序を比較する。（公開手順）
- [A275](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/remove-clips-from-a-sequence.html)　通常削除と後続を詰める削除を同じ区間で比較し、残る隙間とシーケンス終端の時刻を記録する。（公開手順）
