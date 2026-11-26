# 無音短縮の試聴の設計（UX-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

候補ごとに原音と短縮後の試聴区間を切り替え、採用・保留を指定して最後に確定する。

## データと処理境界

候補ID、元範囲、前後の再生余白、保持時間を扱う。字幕文字の変更は候補の採否と別の編集単位にする。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/transcript.rs](../../../../crates/engine/src/transcript.rs)、[crates/edit/src/transcript.rs](../../../../crates/edit/src/transcript.rs)。

確認した関数：[find_pauses](../../../../crates/edit/src/transcript.rs)。語の区間・最小の間・両端に残す量・レートから短縮候補を求める。既存試験は一括短縮を扱う。候補別の原音・短縮案の試聴と取消後の位置復帰は別途実装・検証する。

詳細は[個別の設計書](../../../architecture/edit-graph.md)を参照する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
