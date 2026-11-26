# IO-55 音声ポスト受け渡し — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-55`、受入IDは `AC-IO-55`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

48 kHz素材を中ほどから切り出し前後0.5秒を追加して出力する。対応する受け手で両端を24,000サンプル延長でき、元のカット位置が維持される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [aaf_embedded_trimmed_audio_round_trips_sample_exact](../../../../crates/engine/src/aaf_omf_tests.rs#L57) は <code>file.exportAaf</code> を呼ぶ。
- [aaf_essence_distinguishes_streams_and_linked_refusal_precedes_writes](../../../../crates/engine/src/aaf_omf_tests.rs#L517) は <code>file.exportAaf</code> を呼ぶ。
- [aaf_keeps_a_nested_sequence_as_a_sequence](../../../../crates/engine/src/aaf_omf_tests.rs#L309) は <code>file.exportAaf</code> を呼ぶ。
