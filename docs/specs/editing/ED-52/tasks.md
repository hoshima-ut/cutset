# ED-52 モニターの範囲と挿入 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-52`、受入IDは `AC-ED-52`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

素材[5,15)の音声だけをA2の20へ挿入する。ボタンとキーで得た2案件の配置範囲[20,30)と元素材点は一致し、V1は空。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [reverse_match_frame_finds_the_source_frame](../../../../crates/engine/src/sequence_tools_tests.rs#L96) は <code>sequence.reverseMatchFrame</code> を呼ぶ。
- [match_frame_on_a_nest_loads_the_nested_sequence_at_the_frame_it_shows](../../../../crates/engine/src/nest_editing_tests.rs#L165) は <code>sequence.matchFrame</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。
