# AU-08 役割別の音作り — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-08`、受入IDは `AC-AU-08`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

会話A・音楽BのうちBだけを会話に変更する。Bに会話用設定が表示され、Aの設定値と両配置の元のゲインが変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [auto_match_hits_the_target_loudness](../../../../crates/engine/src/essential_sound_tests.rs#L234) は <code>essentialSound.autoMatch</code> を呼ぶ。
- [auto_match_measures_a_mono_clip_as_one_channel](../../../../crates/engine/src/essential_sound_tests.rs#L273) は <code>essentialSound.autoMatch</code> を呼ぶ。
- [presets_apply_save_and_delete](../../../../crates/engine/src/essential_sound_tests.rs#L211) は <code>essentialSound.set</code> を呼ぶ。
