# アプリ設定の入口の設計（MN-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

アプリメニューまたはコマンド検索から設定を開き、検索結果を選ぶと該当項目にフォーカスする。

## データと処理境界

アプリ共通設定と案件設定を異なる保存先で管理する。外観の変更は画面に反映し、案件履歴を増やさない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/shortcuts.rs](../../../../crates/engine/src/shortcuts.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
