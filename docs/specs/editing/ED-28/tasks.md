# ED-28 ロールトリム — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-28`、受入IDは `AC-ED-28`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

前[0,20)、後[20,50)の境界を+3し、[0,23)と[23,50)を確認する。全尺50、次配置の開始とUndo後の境界20を照合する。

- QA-02　25fpsで連続したA・B各50フレームに十分な前後余白を持たせ、A末尾を3フレーム延長。 期待結果：ロールならAが53、Bが47で全体100。AだけのリップルならAが53、Bが50で全体103。対象外トラックの変化は同期ロック設定ごとに記録。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [split_or_disabled_linked_roll_leaves_audio_alone](../../../../crates/engine/src/trim_tests.rs#L168) は <code>timeline.roll</code> を呼ぶ。
- [roll_delta_is_zero_when_a_clip_cannot_roll_by_the_asked_amount](../../../../crates/engine/src/roll_linked_tests.rs#L77) は <code>timeline.roll</code> を呼ぶ。
- [roll_delta_stops_at_the_start_of_the_media](../../../../crates/engine/src/roll_linked_tests.rs#L52) は <code>timeline.roll</code> を呼ぶ。
