# IO-20 モニターへの情報表示 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

ソース・プログラムの各モニターで名称や時刻の表示を選び、試聴中に切り替える。

## データと処理境界

モニター合成にだけ重ね表示を適用する。書き出しへの焼き込みは別の明示設定として扱う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
