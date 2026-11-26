# マーカーの所属と範囲の作業・試験（ED-55）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-55`、受入IDは `AC-ED-55`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

素材10にマーカーを打ち、素材Inが5の配置を時刻100と200に置く。表示は105と205、元の素材時刻表示は10。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [copy_paste_includes_sequence_markers](../../../../crates/engine/src/sequence_tools_tests.rs#L776) は <code>markers.copyPasteIncludesSequenceMarkers</code> を呼ぶ。
- [ripple_sequence_markers_follow_ripple_edits](../../../../crates/engine/src/sequence_tools_tests.rs#L738) は <code>markers.rippleSequenceMarkers</code> を呼ぶ。
- [flash_cue_markers_round_trip](../../../../crates/engine/src/sequence_extras/tests.rs#L262) は <code>markers.addFlashCue</code> を呼ぶ。

デモ案件でマーカー追加・Undo・Redoを実行し、操作前後のシーケンス全体を照合済み。 [実行記録](../../../verification/marker-history.md)
