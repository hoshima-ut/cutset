# 操作履歴の要件（ED-45）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

編集トランザクションの復元・再適用と診断イベントの閲覧を行う。

## 受入条件

カット→移動→字幕修正を順に戻す。警告の発生時と対象案件を特定できる。

## 例外と復旧

Undo後に別の編集を確定したときは旧Redo枝が使えないことを示す。失敗した編集を履歴に成功として積まない。

## 参照資料と確認項目

- [A243](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/trimming-actions-captured-in-history-panel.html)　同じ境界を続けてトリムし、Historyにまとまる単位とUndoで実際に戻る位置を確認する。（公開手順）
- [A289](https://helpx.adobe.com/premiere/desktop/edit-projects/correct-mistakes/view-warnings-errors-and-information-events.html)　オフライン素材などの既知の事象を発生させ、Eventsで警告・エラー・情報の詳細を読んで原因を識別できるか試す。（公開手順）
- [A290](https://helpx.adobe.com/premiere/desktop/edit-projects/correct-mistakes/view-or-make-changes-in-the-history-panel.html)　Historyから過去の編集状態へ戻ってやり直し、閉じて開いた後は保存した版から再開することを確認する。（公開手順）
