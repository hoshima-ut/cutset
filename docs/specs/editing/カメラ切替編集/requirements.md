# カメラ切替編集の要件（ED-38）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

再生中または停止中に採用する画角を変え、音声固定または画角追従を指定する。

## 受入条件

同一発言中に2回アングルを変え、音声固定の設定で声・位相・尺が連続する。

## 例外と復旧

選んだ角度に映像が存在しない時刻は不足を表示し、固定音声を途切れさせない。

## 参照資料と確認項目

- [A282](https://helpx.adobe.com/premiere/desktop/edit-projects/set-up-multi-camera-sequences-for-editing/create-and-edit-a-multi-camera-target-sequence.html)　マルチカムのターゲットを作り、再生中に3回アングルを切り替え、切替点と固定した録音トラックの連続性を照合する。（公開手順）
- [A285](https://helpx.adobe.com/premiere/desktop/edit-projects/set-up-multi-camera-sequences-for-editing/change-the-order-of-cameras-in-source-and-program-monitors.html)　カメラ表示の順序を入れ替え、各ボタンに対応するカメラ名と実際に切り替わる映像を照合する。（公開手順）
