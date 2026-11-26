# 外部プロキシの対応付けの要件（IO-25）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

原本・代理ファイルの尺・時刻・チャンネルを比較して接続または解除する。

## 受入条件

複数チャンネル音声を含む映像の対応を切り替え、同じフレーム・音声配置か照合。解除で元ファイルが削除されないことを確認。

## 例外と復旧

チャンネル数・時刻の不一致は差分を示し、誤対応を自動で確定しない。解除は対応関係だけを削除する。

## 参照資料と確認項目

- [A180](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/attach-proxies-to-full-resolution-media.html)　既存プロキシを原本に手動で関連付け、似た名前の別テイクと混同せず切り替えられるか試す。（公開手順）
- [A181](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/reconnect-full-resolution-media-to-proxies.html)　プロキシ単独の移動案件に原本を再接続し、最終出力の解像度と素材時刻が原本に戻るか確認する。（公開手順）
- [A182](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/detach-proxies.html)　関連を解除したプロキシが切替対象から外れ、原本に置いたカットと保存フォルダーの実ファイルが変化しないか試す。（公開手順）
- [A219](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/creating-clips-for-offline-editing.html)　低画質で進めたカット列に本編集用素材を接続して、採用フレーム番号と配置順が維持されるか照合する。（公開手順）
- [A220](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/create-low-resolution-clips-for-offline-editing.html)　軽量コピーを作る際にソースタイムコードを残し、後から高解像度の同じフレームへ対応付けられるか試す。（公開手順）
