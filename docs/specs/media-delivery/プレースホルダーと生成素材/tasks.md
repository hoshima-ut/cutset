# プレースホルダーと生成素材の作業・試験（IO-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-11`、受入IDは `AC-IO-11`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同じ赤い下層に黒と透明を順に置く。黒では赤が隠れ、透明では赤が残る。50フレームの仮素材に50フレームの原本を再リンクして境界を比較する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [keyboard_slip_keeps_linked_clips_in_sync_past_the_shorter_handle](../../../../crates/engine/src/clip_ops_tests.rs#L1233) は <code>file.newOfflineFile</code> を呼ぶ。
- [linked_rate_stretch_keeps_one_speed_when_a_neighbour_blocks_the_sound](../../../../crates/engine/src/clip_ops_tests.rs#L1260) は <code>file.newOfflineFile</code> を呼ぶ。
- [linked_slip_keeps_picture_and_sound_aligned_at_unequal_media_limits](../../../../crates/engine/src/clip_ops_tests.rs#L1152) は <code>file.newOfflineFile</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/media/src/generators.rs](../../../../crates/media/src/generators.rs)。
