# モニター操作の配置の要件（UI-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材とシーケンスのモニターごとに操作ボタンの追加・順序を試し、確定または取消できる。

## 受入条件

操作の追加と配置をプレビューし、Cancelで並びを復元する。再生位置、素材のIn/Out、案件の編集履歴は変わらない。

## 例外と復旧

保存済み配列に消滅した操作IDがあれば、その項目を利用不能として扱い、残るボタンを使用できるようにする。

## 参照資料と確認項目

- [A092](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/display-controls-in-the-source-and-program-monitors.html)　モニターに操作ボタンを追加・除去し、並びを変えた後もInsertとOverwriteを目視で区別できるか確かめる。（公開手順）
