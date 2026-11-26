# 二次補正の要件（CO-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

色・彩度・明度から選択領域を抽出して補正し、境界とビネットを調整する。

## 受入条件

肌に近い色の背景を含め、選択マスク・元絵・補正後を比較する。

## 例外と復旧

抽出結果が空のときは該当画素なしと表示する。範囲を広げた結果、背景も含まれた場合はマット表示から調整を続けられる。

## 参照資料と確認項目

- [A493](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/create-masks-using-hsl-and-luminance.html)　該当機能を備える版で輝度範囲と色相範囲を切り替え、同明度の異なる色が選択されるか調べる。（27.0の色・輝度範囲マスク。26系の既存HSL Secondaryと区別）
- [A587](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/correct-color-using-hsl-secondary-controls.html)　対象色の範囲を狭めてマスクを表示し、範囲外が補正されていないか調べる。（公開手順）
- [A625](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/isolated-adjustments-using-masks.html)　マスク境界を横切る対象を補正し、境界外の色と追跡結果を比較する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）

<a id="premiere-27-13"></a>

## HSLマスクと他のマスクを組み合わせる（27.0との照合）

色相、彩度、輝度による被覆率を形状・追跡マスクと組み合わせ、合成順と反転を保存する。[Adobeの公開資料](https://helpx.adobe.com/jp/premiere/desktop/add-video-effects/work-with-masks/create-masks-using-hsl-and-luminance.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-13)と[受入試験](tasks.md#premiere-27-13)に記載する。
