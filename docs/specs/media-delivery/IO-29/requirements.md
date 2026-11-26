# IO-29 キャッシュ管理 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

試聴用データの使用量・保存先を表示し、再生成可能な範囲を選んで掃除する。

## 受入条件

小容量ボリューム上でキャッシュを削除し、素材、案件、編集結果が戻ることを確認。ディスク不足はジョブ失敗と識別する。

## 例外と復旧

再生やレンダーで使用中の項目は保留にする。削除権限が無い項目を削除済みとして数えない。

## 参照資料と確認項目

- [A035](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/memory-preferences.html)　メモリ割当を変え、長時間再生で待ち時間と他アプリとの共存を測る。（公開手順）
- [A751](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/automatically-manage-your-media-cache-files.html)　キャッシュの容量・経過時間の条件に達したとき、原本と案件を削除しない。（障害診断）
- [A752](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/clear-media-cache-on-launch.html)　起動時キャッシュクリア後に案件から波形を再構築できる。（障害診断）
- [A753](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/clear-media-cache-using-preferences.html)　環境設定からキャッシュを消し、削除対象のディスクと回復後の再生を確認する。（障害診断）
- [A754](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/delete-media-cache-files-manually.html)　手動退避したキャッシュを再生成し、元素材のハッシュが一致する。（障害診断）
- [A755](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/manage-media-cache.html)　案件を閉じても残るキャッシュと案件内プレビューを分け、保存先を確認する。（障害診断）
