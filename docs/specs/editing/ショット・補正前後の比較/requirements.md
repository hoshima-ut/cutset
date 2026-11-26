# ショット・補正前後の比較の要件（ED-58）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

別時刻の二つの画または同一時刻の処理前後を並べる。

## 受入条件

違うショットに見える原因が別時刻か効果強度かを、参照時刻表示と分割位置から判別する。

## 例外と復旧

比較用フレームが欠落する場合は対象側だけに欠落と表示し、反対側のキャッシュを流用しない。

## 参照資料と確認項目

- [A615](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/about-comparison-view.html)　参照ショットを固定し、別のフレームを調整しても参照対象が入れ替わらない。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
