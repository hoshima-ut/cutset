# 外部プロキシの対応付けの設計（IO-25）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

外部で作った代理ファイルを選び、原本と比較して接続・解除を切り替える。

## データと処理境界

識別情報、レート、開始時刻、尺、音声構成を照合する。解像度差は代理の属性として保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/proxies.rs](../../../../crates/engine/src/proxies.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
