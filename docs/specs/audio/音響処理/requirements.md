# 音響処理の要件（AU-13）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

EQ・フィルター・ダイナミクス・空間・時間系の処理を配置またはトラックに適用する。

## 受入条件

基準音と音声で適用順・バイパスを確認。パラメトリックEQの周波数・Q・利得と、コンプレッサーの閾値・比率・アタック・リリースの意味を聴取・測定する。

## 例外と復旧

標本化周波数で表せない周波数、非正数のQ等は範囲を示して修正を求める。未対応エフェクトは該当段だけを識別する。

## 参照資料と確認項目

- [A530](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/create-reverb-effect.html)　同じ話者へ異なる響きを加え、文末の残響の長さと原音の聞こえやすさを比較する。（公開手順）
- [A543](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/audio-effects-library.html)　音声効果一覧からEQとディレイを重ね、一つずつバイパスして処理の違いを聞き分ける。（公開手順）
- [A556](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/apply-effects-using-audio-track-mixer.html)　一トラックの効果スロットに遅延を置き、同じトラック上の複数クリップと別トラックを聞き比べる。（公開手順）
- [A557](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/copy-and-paste-audio-effects-in-the-timeline.html)　EQだけを別の音声配置へ貼り付け、元のゲインと個別に付けたフェードを照合する。（公開手順）
- [A558](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/adjust-audio-track-effects-in-timeline.html)　トラック効果のプロパティをタイムラインで表示し、打ったキーによる音色の変化を再生する。（公開手順）
- [A559](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/designate-a-track-effect-as-pre-fade-or-post-fade.html)　コンプレッサーをフェーダー前後で切り替え、フェーダーを下げたときの入力と圧縮量を比較する。（公開手順）
- [A560](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/channelize-effects.html)　多チャンネル信号の指定成分だけへ効果を割り当て、未処理のチャンネルを別々に試聴する。（公開手順）
- [A561](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/copy-and-move-effects-in-audio-track-mixer.html)　ミキサーの挿入効果を別トラックへ複製または移動し、元スロットの有無と適用順を照合する。（公開手順）
