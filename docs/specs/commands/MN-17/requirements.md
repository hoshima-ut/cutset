# MN-17 トラックの一括変更 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

種類、数、位置、対象トラックと保護状態を確認して追加・削除する。

## 受入条件

空のみを削除する場合と指定トラックを削除する場合で、残るトラックとProjectの素材数を確認。

## 例外と復旧

ロック済みの行を含む削除は実行前に通知する。確認以降に配置が追加された行を空扱いで削除しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/delete-tracks.html)
