# FX-04 調整レイヤー — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-04`、受入IDは `AC-FX-04`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

V1に色票、V2の[10,20)に無彩色化、V3に赤いテロップを配置する。10・19だけ背景が無彩色になり、9・20の背景とV3の色は維持される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [cmd_d_on_an_adjustment_layer_fades_its_effects_in_and_out](../../../../crates/engine/src/sequence_extras/tests.rs#L284) は <code>file.newAdjustmentLayer</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/render/src/plan.rs](../../../../crates/render/src/plan.rs)。
- 対応を確認したテスト：[an_adjustment_layer_the_gpu_cant_run_plans_the_frame_on_the_cpu](../../../../crates/render/src/adjustment_tests.rs)。
