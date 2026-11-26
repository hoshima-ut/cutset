# 表示フレームでの検索の要件（MN-33）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

再生中のフレームを指定し、解析能力と結果候補を示す。

## 受入条件

同じ時刻にある別カットをそれぞれ基準にし、選択中のファイル名ではなく画を変えた結果が出るか確認。

## 例外と復旧

空のモニターや解析不能なフレームでは検索を開始しない。解析途中の基準変更は新しい依頼として区別する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/search-for-similar-visuals-using-media-intelligence.html)
