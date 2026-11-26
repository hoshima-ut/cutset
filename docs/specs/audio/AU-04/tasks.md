# AU-04 クリップゲイン — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-AU-04`、受入IDは `AC-AU-04`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

ピーク−12dBFSと−6dBFSの2配置に共通で+3dBを加えると−9と−3になる。各自を−3に正規化すると必要な補正は+9と+3となる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [clip_volume_keys_and_scrub_toggle](../../../../crates/engine/src/keyboard_tests.rs#L262) は <code>clip.volumeDownMany</code> を呼ぶ。
- [audio_gain_modes_and_peak](../../../../crates/engine/src/mixer_tests.rs#L333) は <code>clip.audioGain</code> を呼ぶ。
- [audio_gain_reports_only_audio_items_it_updates](../../../../crates/engine/src/mixer_tests.rs#L364) は <code>clip.audioGain</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/timeline_volume.rs](../../../../crates/ui-egui/src/panels/timeline_volume.rs)。
