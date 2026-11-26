# ED-59 履歴の範囲 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

案件の編集、端末の表示設定、保存済み世代を独立に扱う。

## 受入条件

再起動後にUndoで過去版を戻せると誤案内しない。Auto-Saveの世代からは対象の版を手動で開ける。

## 例外と復旧

再起動してUndo対象がない場合は無効状態と理由を示し、古い自動保存を開く操作へ案内する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/correct-mistakes/view-or-make-changes-in-the-history-panel.html)
