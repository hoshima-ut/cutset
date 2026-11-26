# 音楽の尺合わせの作業・試験（AU-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-11`、受入IDは `AC-AU-11`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同テンポの4秒区間4個から成る曲を12秒に縮める。冒頭と末尾を保護し、中間1区間を除く候補でテンポと保護区間を維持し、接続点を原曲時刻から特定できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [overlaps_are_refused_and_noise_cannot_be_remixed](../../../../crates/engine/src/remix_tests.rs#L150) は <code>clip.remix</code> を呼ぶ。
- [remix_shorter_and_longer_hits_target_at_beats_with_undo](../../../../crates/engine/src/remix_tests.rs#L80) は <code>clip.remix</code> を呼ぶ。
- [menu_commands_and_disabled_reasons](../../../../crates/engine/src/remix_tests.rs#L59) は <code>clip.remix</code> を呼ぶ。
