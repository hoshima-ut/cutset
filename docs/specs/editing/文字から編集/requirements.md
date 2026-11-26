# 文字から編集の要件（ED-42）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

検索・再生・文字訂正と、選んだ発言の映像を変更する操作を分ける。

## 受入条件

「齋藤」を正しても尺と音声は不変。同じ区間を抽出した場合は対応する音声・映像が詰まる。

## 例外と復旧

同じ語が複数配置に現れる場合は使用箇所を選ぶまでタイムラインを変更しない。

## 参照資料と確認項目

- [A221](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/overview-of-text-based-editing.html)　発言テキストと原音の再生位置を往復し、文字列の選択範囲が映像上の発話に対応するか確認する。（公開手順）
- [A222](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/add-clips-to-the-timeline-using-text-based-editing.html)　文字起こし内の2区間を選んでタイムラインに追加し、再生して採用した順と冒頭・末尾の音を照合する。（公開手順）
- [A230](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/multichannel-audio-support-in-text-based-editing.html)　左右に別話者が入る録音で文字起こしに使うチャンネルを変え、得られた文と話者が一致するか聴く。（公開手順）
- [A372](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/find-and-replace-text-in-transcription.html)　文字起こしの一語を検索して置換し、音声波形とシーケンス尺に変更がないか見る。（公開手順）
