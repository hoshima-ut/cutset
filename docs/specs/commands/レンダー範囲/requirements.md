# レンダー範囲の要件（MN-14）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

シーケンス全体、In/Out、選択配置、音声のどこに計算を行うか示す。

## 受入条件

範囲の両側に重い効果を置き、メニューごとにどの区間でプレビューが生成・削除されたか照合。

## 例外と復旧

空の選択範囲は無効と表示する。重なりのない複数選択では、間にある未選択区間を含めるか画面で明示する。

## 参照資料と確認項目

- [公開資料 1](https://colleges.claremont.edu/mediastudies/wp-content/uploads/sites/26/2026/09/helpbook-CC-FALL26B.pdf)
