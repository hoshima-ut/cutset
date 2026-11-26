# IO-30 保存と案件切替 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

複数案件の状態を独立保存し、異常終了後は回復候補を選んで開く。

## 受入条件

保存済み、未保存、オートセーブの各版を比較する。取り込み先での修正とリンク元案件の再オープンを確認。

## 例外と復旧

保存中断や書込不可では直前の保存版と未保存表示を維持する。他案件の復旧候補を上書きしない。

## 参照資料と確認項目

- [A111](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/edit-multiple-open-projects.html)　二つの案件を同時に開き、片側の項目を他方へ取り込み、保存先と変更済み表示を双方で確認する。（公開手順）
- [A112](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/save-workspace-when-editing-multiple-projects-simultaneously.html)　複数案件を開いた配置を保存し、次にそのワークスペースを呼び出して必要なプロジェクトパネルへ到達できるか試す。（公開手順）
- [A113](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/project-locking-with-multiple-open-projects.html)　別利用者が書き込み中の案件を同時に開き、ロックの所有者と読み取り状態を確認して上書きを防げるか試す。（公開手順）
- [A759](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/recover-projects-after-a-crash.html)　最後の手動保存と自動回復コピーを別名で開き、復元した最後の編集を照合する。（障害診断）
