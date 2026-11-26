# 色・画質・重ね表示の要件（IO-44）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

最終変換、色空間と確認用の焼き込み情報を指定する。

## 受入条件

HDR素材のSDRチェック版とHDRマスターを比較し、信号・タグ・黒白の扱いを確認。ウォーターマークが必要な版だけに含まれるか検査。

## 例外と復旧

コンテナが指定タグを保持できないときは出力前に示す。モニター用の表示補正を意図せず焼き込まない。

## 参照資料と確認項目

- [A667](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/add-a-visual-watermark-during-export.html)　ロゴの位置と不透明度を指定し、確認版だけに透かしが入り原本に変化がないか比べる。（公開手順）
