# ガイドの転用の要件（MN-24）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

ガイドを名前付きの組として保存・読み込み・受け渡しする。

## 受入条件

縦型の安全域を別端末に渡し、ガイドの本数・位置をテンプレートの読み込み前後で照合。

## 例外と復旧

未知の版や単位が混じる場合は読み込みを取り消せるようにし、既存の線を消す前に全体を検証する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/save-export-and-import-custom-guides.html)
