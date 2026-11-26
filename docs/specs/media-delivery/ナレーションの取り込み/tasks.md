# ナレーションの取り込みの作業・試験（IO-13）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-13`、受入IDは `AC-IO-13`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

モノラル入力をA2へ送りモニターをミュートして1秒録音する。A2に1配置、音声ファイルには信号があり、A1は変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [an_audio_input_error_stops_and_discards_the_failed_take](../../../../crates/engine/src/voiceover_tests.rs#L102) は <code>audio.voiceover.stop</code> を呼ぶ。
- [record_track_choice_sync_and_discard](../../../../crates/engine/src/voiceover_tests.rs#L229) は <code>audio.voiceover.sync</code> を呼ぶ。
- [settings_persist_in_preferences](../../../../crates/engine/src/voiceover_tests.rs#L138) は <code>audio.voiceover.settings</code> を呼ぶ。
