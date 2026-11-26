# ED-46 保存と世代復旧 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

保存、別名保存、手動復帰、自動バックアップの候補を識別する。

## 受入条件

意図的に異なる3版を作る。復旧後に映像・音・素材参照を照合し、どの版を開いたか確認する。

## 例外と復旧

破損した世代は開けない理由を示して古い世代を選べるようにする。別名保存を中止したら元の保存先を維持する。

## 参照資料と確認項目

- [A027](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/auto-save-preferences.html)　保存間隔と保持世代を設定し、回復コピーから意図した時点の編集を開ける。（公開手順）
- [A696](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/view-auto-saves.html)　公開の間に生じた複数の自動保存から、特定のトリム前の状態を探し出せるか確認する。（公開手順）
