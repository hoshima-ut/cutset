# 変形とアンカーの作業・試験（FX-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-08`、受入IDは `AC-FX-08`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

100×50の図形を左上アンカーで2倍にする。左上の表示位置は固定され、200×100になる。90度回転で同じ基準点を中心に長辺の向きが変わる。

- QA-07　番号と色チャート付きの動く素材を縮小し、対象にマスクを重ねる。低解像度プレビューと縮小出力を作る。 期待結果：マスクの有無と向き、境界、上下のレイヤー、色空間を参照と比較。26.5.3の修正対象だった条件も試す。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [fit_and_fill_frame](../../../../crates/engine/src/clip_ops_tests.rs#L646) は <code>clip.fillFrame</code> を呼ぶ。
- [fit_and_fill_frame_scale_a_nest_to_the_sequence](../../../../crates/engine/src/nest_fidelity_tests.rs#L44) は <code>clip.fillFrame</code> を呼ぶ。
- [scale_to_frame_size_on_a_nest_fills_the_frame_and_leaves_scale_alone](../../../../crates/engine/src/nest_fidelity_tests.rs#L57) は <code>clip.scaleToFrameSize</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/transform_handles.rs](../../../../crates/ui-egui/src/panels/transform_handles.rs)。
