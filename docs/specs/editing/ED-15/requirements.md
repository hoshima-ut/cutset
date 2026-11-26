# ED-15 挿入・上書き — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

差し込んで後続を送るか、指定範囲だけ置換するかを選ぶ。

## 受入条件

途中の10フレームに挿入すると後続が10フレーム動く。同長の上書きは後続の開始点を保つ。

## 例外と復旧

ロックや無効なパッチで全要素を配置できない場合は編集前の状態を返し、音声だけを残さない。

## 参照資料と確認項目

- [A203](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/add-or-remove-clips.html)　中央へ1クリップを追加後にリップル削除し、もとの順序と全体尺に戻るかを確かめる。（公開手順）
