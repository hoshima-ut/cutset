# 二つのモニターの設計（UI-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材を左モニターに開き、右側の同じ素材の配置を別時刻で停止する。選択したモニターだけを再生し、範囲を設定する。

## データと処理境界

素材側は素材ID・素材時刻・範囲、完成側はシーケンスID・シーケンス時刻・範囲を持つ。キー操作の送信先をフォーカスで解決する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)、[crates/ui-egui/src/source_playback.rs](../../../../crates/ui-egui/src/source_playback.rs)。

確認した関数：[start_source_playback](../../../../crates/ui-egui/src/source_playback.rs)。素材再生には専用の開始位置・停止位置・速度を渡す。既存UIテストはフォーカス先と音の排他再生を確認する。候補レビューから戻った際の両モニター位置は追加検証が必要。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
