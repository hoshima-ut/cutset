# IO-10 素材の解釈 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-10`、受入IDは `AC-IO-10`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25 fpsで100フレームの素材を50 fpsと解釈し、素材尺が4秒から2秒へ変わること、元設定に戻すと4秒になることを確認する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [interpret_footage_pixel_aspect_wins_over_the_file_and_undoes](../../../../crates/engine/src/par_tests.rs#L119) は <code>clip.interpretFootage</code> を呼ぶ。
- [field_options_and_time_interpolation_are_stored](../../../../crates/engine/src/clip_ops_tests.rs#L540) は <code>clip.fieldOptions</code> を呼ぶ。
- [modify_timecode_and_reset](../../../../crates/engine/src/clip_ops_tests.rs#L459) は <code>clip.modifyTimecode</code> を呼ぶ。
