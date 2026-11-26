# FX-01 効果の検索 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

検索語で候補を絞り、対象が映像か音声か、処理精度、端末で利用できる経路を個別に指定する。選択すると適用先と効果名を読み上げる。

## データと処理境界

効果IDと版を永続識別子にする。検索結果ごとに対応精度とCPU/GPU実行可否を独立して返し、案件で使用中の旧IDも識別する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/effects.rs](../../../../crates/ui-egui/src/panels/effects.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
