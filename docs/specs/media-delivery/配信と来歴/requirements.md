# 配信と来歴の要件（IO-49）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

完成ファイルを出力先に渡し、ウォーターマークや出所情報の有無を確認する。

## 受入条件

承認済みの検証先を使用し、保存と外部公開を区別する。認証失効時の状態、付与した著作者・利用意思情報の閲覧可否を確認。

## 例外と復旧

認証失効時はローカル出力を保持する。送信済みか不明な再試行は送信先の結果と照合してから扱う。

## 参照資料と確認項目

- [A646](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/best-practices-for-exporting-video-for-social-media-and-phones.html)　縦型スマートフォン用の確認動画を実端末で再生し、画角、UIに隠れる字幕、音声を点検する。（公開手順）
- [A647](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-videos-for-social-media-channels.html)　検証用の配信先を選び、公開範囲と保存先を確認してからローカル出力と配信結果を別々に記録する。（公開手順）
- [A650](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-videos-with-content-credentials.html)　来歴情報を付けた成果物と外した成果物を比較し、作成者情報と公開の選択が反映されたか読む。（26.2で書き出しにContent Credentialsを追加）
- [A731](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/export-for-viewing-platforms.html)　同じ番組から放送用横型と配信用縦型を出力し、字幕の画面内位置と納品プリセットを読み戻す。（公開手順）
