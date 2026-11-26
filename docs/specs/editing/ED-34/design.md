# ED-34 速度の時間変化 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

速度の変化点を追加し、隣接区間の速度と補間を指定して変化前後の素材位置を試聴する。

## データと処理境界

各区間の再生率を時間に沿って積分して素材時刻を求める。保持区間と逆向き区間を識別し、補間処理への入力フレームを決定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/linked_speed_tests.rs](../../../../crates/engine/src/linked_speed_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
