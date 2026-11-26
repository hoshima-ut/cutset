# 時間と整列の表示の設計（UI-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

時間表示をフレームとタイムコードで切り替え、ガイドを定規から追加し、スナップを切り替えて配置する。

## データと処理境界

時刻は内部tickで保持し、表示だけをレートとドロップ規則で変換する。モニターのガイドはフレーム座標で保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/timecode.rs](../../../../crates/ui-egui/src/panels/timecode.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
