# IO-32 プレビューの計算 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-32`、受入IDは `AC-IO-32`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

0〜49、50〜99の2区間を計算し、後半の効果だけを変更する。前半は利用可能なまま、後半だけが再計算対象になる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [render_in_to_out_renders_only_the_marked_frames](../../../../crates/engine/src/previews_tests.rs#L167) は <code>sequence.renderInToOut</code> を呼ぶ。
- [render_selection_and_audio_previews](../../../../crates/engine/src/previews_tests.rs#L254) は <code>sequence.renderSelection</code> を呼ぶ。
- [an_audio_segment_too_long_for_a_wav_fails_the_job](../../../../crates/engine/src/previews_tests.rs#L413) は <code>sequence.renderAudio</code> を呼ぶ。
