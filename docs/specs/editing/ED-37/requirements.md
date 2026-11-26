# ED-37 複数カメラの同期 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

基準時刻、同期点または音声で複数テイクと外部収録音を揃える。

## 受入条件

同じ手拍子が全アングルで一致。基準点がない素材、重複カメラ名、片方だけ遅く録画開始したケースを記録する。

## 例外と復旧

相関が弱い、または基準点がない素材は未同期に残す。使用者が同期点を設定してから角度群へ加える。

## 参照資料と確認項目

- [A281](https://helpx.adobe.com/premiere/desktop/edit-projects/set-up-multi-camera-sequences-for-editing/create-a-multi-camera-source-sequence.html)　TC同期と音声同期で同じ2カメラを束ね、クラップの立ち上がりと同じ映像イベントのずれを測る。（公開手順）
- [A283](https://helpx.adobe.com/premiere/desktop/edit-projects/set-up-multi-camera-sequences-for-editing/mark-clips-for-synchronization.html)　映像と別録り音声に共通名の同期マーカーを打ち、2本の開始時刻が違っても同じ瞬間が重なるか試す。（公開手順）
- [A284](https://helpx.adobe.com/premiere/desktop/edit-projects/set-up-multi-camera-sequences-for-editing/manage-multi-camera-thumbnails-in-the-project-panel.html)　ビン内のマルチカム項目のサムネイル表示を切り替え、編集用シーケンスの採用アングルに影響しないか確認する。（公開手順）
