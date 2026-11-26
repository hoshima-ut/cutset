# MN-02 案件の取り込みポリシー — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

案件を選び、コピー・変換・プロキシ設定と今後の適用範囲を確認する。

## 受入条件

一つのファイルを参照と複製の二方式で取り込む。参照では原本、複製では指定先の複製を開き、取り消した取り込みは一覧に残らない。

## 例外と復旧

複製先が書込不可なら参照取り込みへ勝手に切り替えず、保存先を再指定できる。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/configure-ingest-settings.html)
