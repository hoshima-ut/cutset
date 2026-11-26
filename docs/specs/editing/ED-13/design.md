# ED-13 ロックと連動 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

トラックの編集ロックと同期ロックを個別に設定し、挿入前に後続で動くトラックを確認する。

## データと処理境界

対象トラック集合と同期移動対象集合から差分を計算する。編集ロック済みのトラックの配置を動かす案は採用できない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/locked_clip_edits_tests.rs](../../../../crates/engine/src/locked_clip_edits_tests.rs)、[crates/edit/src/lib.rs](../../../../crates/edit/src/lib.rs)。

確認した関数：[ripple_delete_items](../../../../crates/edit/src/lib.rs)。削除対象の区間を統合して後続を詰める演算がある。同期ロック字幕の移動とUndoをエンジン試験で扱う。候補一覧への影響対象の提示は追加設計。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
