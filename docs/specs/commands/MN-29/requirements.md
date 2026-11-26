# MN-29 プロキシ生成の入口 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

選択素材の生成可否と理由を示し、処理完了後に同じ対象へ割り当てる。

## 受入条件

原本が読める動画では代理素材の生成が一回だけ開始する。欠落素材には対象IDと読み取り不能の理由が出て、空ジョブを作らない。

## 例外と復旧

同一素材の同条件ジョブが進行中なら既存ジョブを開く。欠落原本だけの選択では実行できない理由を読むことができる。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/create-proxies.html)
