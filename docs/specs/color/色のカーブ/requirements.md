# 色のカーブの要件（CO-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

RGB、色相、輝度、彩度のカーブを操作し、一部の色域だけ変更する。

## 受入条件

赤いユニフォームだけを少し変え、肌や暗部の中立色の変化を確認する。

## 例外と復旧

同じ入力位置に矛盾する点を置く操作は既存点の編集として示す。カーブを初期化すると選択したチャンネルだけが恒等に戻る。

## 参照資料と確認項目

- [A579](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/correct-color-using-rgb-curves.html)　赤のカーブだけを曲げ、RGBパレードで他のチャンネルへの影響を照合する。（公開手順）
- [A580](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/correct-color-using-hue-and-saturation-curves.html)　特定色相だけ彩度を下げ、別色のパッチと肌色の変化を比較する。（公開手順）
