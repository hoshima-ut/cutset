# IO-02 選択トレイ — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材をトレイに並べ、順番の変更・除外・取り込み先ビンの指定を行う。確定前に対象数を表示する。

## データと処理境界

一覧は順序付きの候補と取り込み方法を保持する。案件への登録は確定時に行い、選択順を下流のシーケンス作成へ引き渡す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/import_mode.rs](../../../../crates/ui-egui/src/panels/import_mode.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
