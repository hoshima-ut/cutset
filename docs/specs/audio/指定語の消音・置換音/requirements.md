# 指定語の消音・置換音の要件（AU-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

発言の検索結果を試聴し、選んだ区間だけを消音または信号音で隠す。

## 受入条件

似た固有名詞、同音語、音楽との重なりで対象時刻を試聴し、誤検出のみ取り消せるか確認する。

## 例外と復旧

確信度の低い一致や再リンクで変化した区間は要確認とする。フェードの余白が隣接した保護区間へ食い込むときは境界を表示する。

## 参照資料と確認項目

- [A522](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/clean-audio-with-bulk-mute-or-bleep.html)　指定語の複数出現の一方だけに警告音を適用し、ほかの発音と映像尺を保ったか聴く。（25.6正式版の一括ミュート・ビープを継承）
