# IO-54 編集決定リスト — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

リールとタイムコードに基づくカット一覧を渡し、複数トラック等の変換損失を示す。

## 受入条件

固有のリール名・重複ファイル名を持つ2テイクで先頭素材と最終カットが一致するか確認。29.97 DFを別に検証。

## 例外と復旧

同一リール名が複数原本を指す場合は解決を促す。多層合成や可変速を単純なカットとして報告しない。

## 参照資料と確認項目

- [A648](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-project-as-an-edl-file.html)　別リールの同名素材を含むEDLから、各カットのリールと元・出力タイムコードを復元する。（公開手順）
