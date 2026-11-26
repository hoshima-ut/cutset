# 音声明瞭化の要件（AU-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

会話のノイズ・残響を補正し、原音と処理音の混合量を調整する。

## 受入条件

観客の歓声の中の声で、本人の呼吸・声質まで失われないか確認する。元に戻して再生できる。

## 例外と復旧

声を識別できない区間やモデル欠落時は原音を再生し、未処理範囲を知らせる。再解析で旧結果を破棄する前に利用可能な処理結果を確保する。

## 参照資料と確認項目

- [A512](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/separate-overlapping-speakers.html)　話者分離に対応する版で重なった会話だけを選び、生成された各話者音声と原音を個別に聴く。（27.0正式のSeparate Crosstalk。26系正式の対象外）
- [A526](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/enhance-speech.html)　雑音のある台詞を強調し、26系では原音との混合量を変えて子音と環境音を聞き比べる。（既存のEnhance Speech。27.0のRTX高速化・Enhance Audio新版と区別）
- [A528](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/improve-dialogue-clarity.html)　聞き取りにくい声に明瞭度の調整を行い、囁きと大きな台詞で歯擦音の出方を比べる。（公開手順）
- [A529](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/repair-dialogue.html)　ハムと残響のある台詞を個別に修復し、どちらの調整でどの雑音が減ったか確認する。（公開手順）
- [A538](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/enhance-speech-technical-requirements.html)　対象端末の機器・モデル要件を照合し、短い台詞で処理可否と案内された理由を記録する。（公開手順）
- [A541](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/enhance-audio-overview.html)　Enhance Audio対応版で混在音を解析し、声・背景など各成分を一つずつ変えた結果を比較する。（27.0で正式提供。26系のEnhance Speechと音声分離を含むEnhance Audioを区別）
- [A542](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/apply-enhance-audio-to-clips.html)　処理するクリップを一つに限定して分離量を変更し、隣のクリップと元音声が保存されるか確認する。（27.0で正式提供。26系のEnhance Speechと音声分離を含むEnhance Audioを区別）
- [A778](https://helpx.adobe.com/premiere/desktop/troubleshooting/audio-issues/enhance-speech-is-running-slow.html)　音声強調の処理中も元音声を試聴でき、完了・取消時の状態を追跡できる。（障害診断）

## 会話音声の成分別調整

対応モデルの音声成分と調整可能な値を表示する。

[設計](design.md#会話音声の成分別調整) ・ [受入試験](tasks.md#会話音声の成分別調整)

## 重なって話す二人の声を分離する

単一のミックスから時間原点を共有する二つの音声素材を作る。

[設計](design.md#重なって話す二人の声を分離する) ・ [受入試験](tasks.md#重なって話す二人の声を分離する)
