# 案件の再開の設計（UI-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

最近開いた一覧から案件を選び、読み込み完了後に最後のシーケンスに戻る。所在不明なら場所を指定できる。

## データと処理境界

一覧には案件識別子・保存先・最終操作時刻を保持し、案件を開けた時点で履歴を更新する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/import_mode.rs](../../../../crates/ui-egui/src/panels/import_mode.rs)、[apps/filmcraft/src/main.rs](../../../../apps/filmcraft/src/main.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
