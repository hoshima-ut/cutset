# MN-18 マーカー付き貼り付け — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

コピー時にマーカーの同行を選び、別シーケンスの貼り付け開始位置を指定する。

## データと処理境界

対象シーケンスマーカーをコピー範囲の相対時刻へ変換する。貼り付け先で新しいIDを発行し、色・注記・長さを複製する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/marker_edit.rs](../../../../crates/engine/src/marker_edit.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
