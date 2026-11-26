# AU-07 ミックスオートメーション — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

読み取り・書き込み・タッチ・ラッチ各モードで既存カーブへの変更を制御する。

## 受入条件

同じ操作をTouchとLatchで行い、手を離した後のキーと再生結果に差がある。

## 例外と復旧

再生中断やデバイス切断では最後に確定した時刻で記録を終了し、書込み状態を解除する。再開だけで未操作の区間を上書きしない。

## 参照資料と確認項目

- [A555](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/record-changes-to-sound-tracks.html)　トラックを再生しながら一回だけ音量を下げ、再生し直すと同じ時間で変化するか試す。（公開手順）
- [A562](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/audio-track-mixer-automation-modes.html)　同じフェーダー操作をTouchとLatchで記録し、指を離した後のカーブを比較する。（公開手順）
- [A563](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/set-automatch-time-for-touch-mode-and-read-mode.html)　自動復帰時間を短くした場合と長くした場合で、手を離してから元カーブに戻る時間を測る。（公開手順）
- [A564](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/specify-automated-keyframe-creation.html)　自動キー記録の間隔・最適化設定を変え、一定速度のフェーダー操作から生成されるキー数を比べる。（公開手順）
