# 配置のミキシングの作業・試験（AU-05）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-05`、受入IDは `AC-AU-05`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

[100,150)の配置のローカル20に−6dBのキーを打ち、配置を10フレーム後へ移す。タイムラインの130で同じキーが効き、旧位置120にはキーが残らない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [clip_mixer_release_commits_to_the_clip_that_was_grabbed](../../../../crates/engine/src/mixer_tests.rs#L516) は <code>clipMixer.release</code> を呼ぶ。
- [clip_mixer_touch_writes_clip_keyframes_and_ramps_back](../../../../crates/engine/src/mixer_tests.rs#L435) は <code>clipMixer.touch</code> を呼ぶ。
- [clip_automation_spanning_two_clips_writes_both](../../../../crates/engine/src/mixer_tests.rs#L558) は <code>clipMixer.setMode</code> を呼ぶ。
