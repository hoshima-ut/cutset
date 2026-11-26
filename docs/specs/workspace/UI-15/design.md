# UI-15 外部入出力の調整 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

入出力機器とチャンネルを選び、テスト信号を左右へ順に出して遅延を調整する。

## データと処理境界

デバイスID、サンプルレート、バッファ長、チャンネル割当、映像との監視遅延を保持する。監視遅延は作品の音声位置に足さない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/settings.rs](../../../../crates/ui-egui/src/panels/settings.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
