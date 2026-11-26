# プロキシ接続の入口の要件（MN-30）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

候補ファイルの時間・映像・音声構成を照合して接続する。

## 受入条件

原本が欠落しても照合可能な代理素材は明示的に接続できる。尺や音声構成が衝突する候補は差を示し、自動で接続しない。

## 例外と復旧

開始時刻や音声構成が衝突した候補を自動接続しない。確定の取消で既存のプロキシ参照を維持する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/attach-proxies-to-full-resolution-media.html)
