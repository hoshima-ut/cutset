# スリップの作業・試験（ED-29）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-29`、受入IDは `AC-ED-29`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

配置[20,70)、素材[100,150)を+3スリップすると素材[103,153)、配置[20,70)のまま。試聴の両端と確定後の画が一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [hostile_slip_preview_params_are_errors_or_clamped_never_panics](../../../../crates/engine/src/slip_tests.rs#L215) は <code>timeline.slipPreview</code> を呼ぶ。
- [the_preview_is_what_the_slip_commits_for_every_delta](../../../../crates/engine/src/slip_tests.rs#L52) は <code>timeline.slip</code> を呼ぶ。
- [sound_only_clips_preview_without_pictures](../../../../crates/engine/src/slip_tests.rs#L157) は <code>timeline.slip</code> を呼ぶ。
