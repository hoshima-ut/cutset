# 形状マスクの作業・試験（FX-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-10`、受入IDは `AC-FX-10`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

200×200の市松模様に中央100×100の矩形を描く。ぼかしに割り当てたとき外側は原画、不透明度に割り当てたとき外側は透明になる。

- QA-07　番号と色チャート付きの動く素材を縮小し、対象にマスクを重ねる。低解像度プレビューと縮小出力を作る。 期待結果：マスクの有無と向き、境界、上下のレイヤー、色空間を参照と比較。26.5.3の修正対象だった条件も試す。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [add_vertex_on_animated_path_clamps_oversized_index_and_rejects_empty_path](../../../../crates/engine/src/masks_tests.rs#L110) は <code>masks.add</code> を呼ぶ。
- [background_tracking_is_applied_without_a_ui_frame_loop](../../../../crates/engine/src/masks_tests.rs#L440) は <code>masks.track</code> を呼ぶ。
- [every_project_replacing_path_drops_pending_tracking_jobs](../../../../crates/engine/src/masks_tests.rs#L493) は <code>masks.track</code> を呼ぶ。
