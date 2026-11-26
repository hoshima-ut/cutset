# 音声フェードの要件（AU-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

両端または片端に音量遷移を置き、長さとゲイン曲線を選ぶ。

## 受入条件

相関の高い同相信号と独立した環境音で、切替中点のピークと知覚音量がどう変わるかを確認する。

## 例外と復旧

必要な素材余長がない側は不足量を表示し、フェード範囲の短縮・片側への変更を選ばせる。

## 参照資料と確認項目

- [A566](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-transitions/crossfade-between-audio-clips.html)　二つの独立した環境音の境界にクロスフェードを置き、切替中点に無音や急な突起がないか聴く。（公開手順）
- [A567](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-transitions/fade-in-or-fade-out-clip-audio.html)　台詞の終端だけにフェードアウトを置き、先頭と隣クリップの立ち上がりが変わらないか確認する。（公開手順）
- [A568](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-transitions/specify-default-audio-transitions.html)　音声の既定トランジションを変更し、新しい境界へ適用した効果名・尺を確認する。（公開手順）
- [A569](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-transitions/audio-crossfade-transitions.html)　同じ二入力で一定ゲイン・一定パワー・指数フェードを比較し、中間時刻のレベル差を測る。（公開手順）
