# ED-10 タイムライン移動 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

編集点、時刻、クリップ検索、ズームを使って狙った配置に移動する。

## 受入条件

同名シーケンスを別案件に作り、現在開いた方だけに変更が入る。

## 例外と復旧

移動先の配置が編集済みで消えていれば該当タブで結果を再検索し、同名の別シーケンスへ移動しない。

## 参照資料と確認項目

- [A252](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/navigation-controls-in-the-timeline.html)　タイムルーラー、再生ヘッド、ズームバーを順に動かして、どの操作が表示範囲だけを変えるか確認する。（公開手順）
- [A253](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/navigate-sequences-in-the-timeline.html)　異なるシーケンスタブを行き来し、対象トラック上の次の編集点へ飛んだ時刻をタブごとに照合する。（公開手順）
