# IO-10 素材の解釈 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

フレームレート・画素比・フィールド・アルファ・色の解釈を上書きする。

## 受入条件

25 fps素材を別fpsで解釈し、変化した尺を記録。アナモフィック映像の円と半透明の縁で比率・合成も照合。

## 例外と復旧

尺の短縮で参照範囲が不足するときは該当配置と不足量を提示し、確認前にタイムラインを変更しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/modifying-clip-properties-with-interpret-footage.html)
