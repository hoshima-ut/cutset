# MN-14 レンダー範囲 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

レンダーメニューで全体・In/Out・選択・音声を区別し、開始前に実際の時間範囲を表示する。

## データと処理境界

範囲と対象メディアをプレビュー処理へ渡す。削除時も同じ時間基準を使い、範囲外の生成物を維持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/previews.rs](../../../../crates/engine/src/previews.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
