# カット点検出の作業・試験（ED-25）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-25`、受入IDは `AC-ED-25`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

既知境界25・50・75と1フレームの白フラッシュを含む映像を使い、候補と正解を比較する。フラッシュを除外後、採用した境界だけが分割される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [background_job_reports_progress_and_cancel_changes_nothing](../../../../crates/engine/src/scene_detect/tests.rs#L118) は <code>clip.sceneEditDetection</code> を呼ぶ。
- [detects_cuts_in_our_own_render_and_applies_cuts_markers_and_subclips](../../../../crates/engine/src/scene_detect/tests.rs#L63) は <code>clip.sceneEditDetection</code> を呼ぶ。
- [detects_the_cuts_of_an_ffmpeg_concat_and_cuts_linked_audio](../../../../crates/engine/src/scene_detect/tests.rs#L177) は <code>clip.sceneEditDetection</code> を呼ぶ。
