# IO-22 類似フレーム検索 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

表示フレームで検索し、解析済み範囲と古くなったインデックスを区別する。

## 受入条件

素材ごとの解析結果を別案件で再利用し、索引だけを失った場合の再生成を確認。解析途中も手編集できるか試す。

## 例外と復旧

同じパスの内容が変わったら旧索引を失効させ、再構築できる。解析失敗で案件や素材を変更しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/search-for-similar-visuals-using-media-intelligence.html)
- [公開資料 2](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/manage-media-intelligence-metadata.html)
