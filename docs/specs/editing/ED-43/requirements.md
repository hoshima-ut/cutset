# ED-43 間・フィラー・話者の選別 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

発言の候補範囲を試聴して個別または一括で残す・詰めるを決める。

## 受入条件

無音が続く候補2件のうち「答えに迷った間」を残す。変更した区間と後続編集点を照合する。

## 例外と復旧

発言境界が変わった候補は再計算を求め、古い検出時刻で変更を確定しない。

## 参照資料と確認項目

- [A225](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/detect-and-delete-pauses-in-transcripts.html)　長さの異なる二つの沈黙を抽出し、選んだ一方を詰めた後も残した間と前後の語尾を聞き取れるか試す。（公開手順）
- [A229](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/remove-all-instances-of-one-speaker-in-transcript.html)　話者を一人だけ除去し、似た声の別話者と重なり発話に対する誤削除の有無を原音で確認する。（公開手順）
