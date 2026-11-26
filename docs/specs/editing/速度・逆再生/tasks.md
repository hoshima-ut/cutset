# 速度・逆再生の作業・試験（ED-33）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-33`、受入IDは `AC-ED-33`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

48フレームを倍速にして尺24、逆向きでは先頭側の画が素材終端側になる。後続リップルの有無で次配置の開始差24を確認する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [faster_with_ripple_moves_later_clips_once](../../../../crates/engine/src/linked_speed_tests.rs#L52) は <code>clip.speedDuration</code> を呼ぶ。
- [maintain_audio_pitch_goes_with_the_clip_and_its_sound](../../../../crates/engine/src/linked_speed_tests.rs#L157) は <code>clip.speedDuration</code> を呼ぶ。
- [maintain_audio_pitch_leaves_a_locked_linked_sound_alone](../../../../crates/engine/src/linked_speed_tests.rs#L189) は <code>clip.speedDuration</code> を呼ぶ。

## 音声の時間伸縮方式と音程を選ぶ

- [ ] 4秒の基準音を50%で8秒にし、音程保持と音程変更を個別に試す。再読込後の尺と、指定した基音の変化を出力音声で測る。
