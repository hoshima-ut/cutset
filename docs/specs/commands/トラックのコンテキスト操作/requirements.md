# トラックのコンテキスト操作の要件（MN-34）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

ポインター・キーから対象行の属性、追加・削除を選ぶ。

## 受入条件

クリップ、空白、ヘッダー上で右クリックして項目を比較。追加のキャンセルで既存トラック数が変わらないか確認。

## 例外と復旧

表示中にトラックが並べ替えられても旧行番号で別トラックを操作しない。ロックや削除済みの対象では実行を中止する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/add-tracks.html)
