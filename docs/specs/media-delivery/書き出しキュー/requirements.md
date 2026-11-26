# 書き出しキューの要件（IO-48）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

版と出力設定を固定したジョブを複数登録し、個別に停止・再試行する。

## 受入条件

横・縦の2本をキューに入れ、一方を停止して再実行。停止したジョブの部分出力、他ジョブ、元案件に与える影響を確認。

## 例外と復旧

中断した仮ファイルを完成品にしない。再試行時に出力先競合を再検査し、他のジョブの状態を維持する。

## 参照資料と確認項目

- [A652](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-directly-to-adobe-media-encoder.html)　音声と縦動画のジョブをMedia Encoderに送り、両方の設定が分かれて入り元案件を編集し続けられるか試す。（公開手順）
