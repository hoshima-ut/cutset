# 書き出し状況の要件（UI-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

対象版、範囲、出力内容、進捗、停止理由を同じジョブから追跡する。

## 受入条件

現在の版、出力範囲、映像・音声・字幕、進捗、失敗区間を確認できる。書き出し中の手編集と出力に使った版を区別して履歴に残す。

## 例外と復旧

出力途中の書込失敗は失敗位置と理由を保存する。完成済み出力への置換は正常終了まで行わない。

## 参照資料と確認項目

- [A771](https://helpx.adobe.com/premiere/desktop/troubleshooting/export-issues/unable-to-find-the-cause-of-render-or-export-issue.html)　尺を二分して出力し、書き出しが失敗する最小区間を特定する。（障害診断）
- [A772](https://helpx.adobe.com/premiere/desktop/troubleshooting/export-issues/export-is-very-slow.html)　符号化方式・素材・効果を一つずつ変え、時間を使った工程を記録する。（障害診断）
- [A773](https://helpx.adobe.com/premiere/desktop/troubleshooting/export-issues/unable-to-render-or-export-a-specific-project.html)　特定案件だけで失敗する場合に別案件への部分移送で原因クリップを絞る。（障害診断）
- [A774](https://helpx.adobe.com/premiere/desktop/troubleshooting/export-issues/unable-to-render-or-export-premiere-project.html)　書き出し失敗時に未完成ファイルを識別し、元案件から同じ設定で再実行する。（障害診断）
