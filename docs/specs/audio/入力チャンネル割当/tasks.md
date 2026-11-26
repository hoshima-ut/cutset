# 入力チャンネル割当の作業・試験（AU-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-01`、受入IDは `AC-AU-01`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

左に440Hz、右に880Hzを収録した素材の左右を入れ替える。書き出しでは左880Hz・右440Hzになり、原本を直接再生すると元の割当が保たれる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [audio_channels_rejects_a_channel_less_call_with_no_item_selected](../../../../crates/engine/src/clip_ops_tests.rs#L445) は <code>clip.audioChannels</code> を呼ぶ。
- [extract_audio_writes_a_wav_and_imports_it](../../../../crates/engine/src/clip_ops_tests.rs#L666) は <code>clip.extractAudio</code> を呼ぶ。
- [modify_audio_channels_and_breakout_to_mono](../../../../crates/engine/src/clip_ops_tests.rs#L391) は <code>clip.audioChannels</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/audio-dsp/src/channels.rs](../../../../crates/audio-dsp/src/channels.rs)。
