# 再圧縮の回避の要件（IO-45）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

設定が適合する区間でプレビューまたはソースを再利用し、再圧縮する範囲を識別する。

## 受入条件

同一設定のProResまたは対応MXFで、カットだけの区間と効果区間を混在させて画質・処理時間を記録。形式を変えて再比較。

## 例外と復旧

適合性を証明できない区間は再符号化し、理由を記録する。古いプレビューを別版に流用しない。

## 参照資料と確認項目

- [A638](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/smart-rendering-supported-formats.html)　同じ中間コーデックのカットだけの区間と効果付き区間を出力し、再圧縮を省ける条件を切り分ける。（26.5でXAVC-Iの一部にSmart Renderingを拡張）
