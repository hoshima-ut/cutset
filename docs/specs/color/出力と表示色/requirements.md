# 出力と表示色の要件（CO-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

表示用変換と納品用のSDR・HLG・PQ変換を別々に指定する。

## 受入条件

同じシーケンスのファイルを再読込し、色空間タグ、スコープ、対象表示環境を記録する。

## 例外と復旧

HDR表示に対応しない端末ではSDR確認用変換の使用を表示する。コーデックが必要なタグに対応しない場合は出力前に知らせる。

## 参照資料と確認項目

- [A599](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/configure-sequence-output-color-space.html)　納品色空間を切り替え、書き出しのタグと表示用変換を照合する。（公開手順）
