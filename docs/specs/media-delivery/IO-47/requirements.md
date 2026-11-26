# IO-47 フレームと連番出力 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

時刻または範囲を指定し、色・アルファと番号順を保って静止画に出す。

## 受入条件

末尾フレームをPNGで保存し、ソースとシーケンスの表示の違い、アルファ・時刻と連番の通し番号を照合。

## 例外と復旧

出力の途中に既存ファイルがある場合は競合名を先に提示する。未確認の上書きや無断での欠番を避ける。

## 参照資料と確認項目

- [A640](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-still-frame.html)　プログラムモニターで1フレームだけ保存し、現在のフレーム番号と静止画の内容を照合する。（公開手順）
- [A641](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-still-image.html)　透過を含む画像の出力形式と保存先を指定し、再読み込み時の寸法とアルファを確認する。（公開手順）
