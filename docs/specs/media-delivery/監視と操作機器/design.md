# 監視と操作機器の設計（IO-28）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

映像監視先、音声先、コントローラーを個別に選択し、同期用の画とクリックを出す。

## データと処理境界

デバイスIDと役割、対応レート、設定した遅延補正を保持する。画面上の操作とデバイス入力は同じ編集命令へ渡す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/settings.rs](../../../../crates/ui-egui/src/panels/settings.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
