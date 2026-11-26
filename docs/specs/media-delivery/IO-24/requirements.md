# IO-24 プロキシの生成 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

原本と対応付く軽量ファイルをバックグラウンドで生成する。

## 受入条件

生成中に別の素材を編集。生成失敗の再試行で同じ素材に複数の対応が生まれないよう確認。

## 例外と復旧

処理中に原本が交換されたら古い出力を自動接続しない。再試行時は同じ完成済みの代理を重複登録しない。

## 参照資料と確認項目

- [A179](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/create-proxies.html)　高解像度素材からプロキシを生成し、元の尺・時刻・チャンネルの対応を冒頭と末尾で照合する。（公開手順）
