# AU-17 試聴の一括消音 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

既存のトラック設定を保持してモニター音全体を一時的に消す。

## 受入条件

元からミュート中のトラックが全体消音解除後も鳴らない。書き出し品質の検証は別に行う。

## 例外と復旧

出力機器の切断と一括消音を別状態で示す。機器再接続でトラックミュートやソロを解除しない。

## 参照資料と確認項目

- [A540](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/global-mute.html)　もともと一トラックだけミュートした状態で全体を消音し、解除後に元の個別設定が残るか聴く。（26.2でシーケンスのGlobal Mute追加）
