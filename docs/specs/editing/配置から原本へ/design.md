# 配置から原本への設計（ED-23）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

プレイヘッド下の対象トラックを選び、フレーム照合で素材モニターを開いて元の前後を試聴する。

## データと処理境界

配置開始からの時間差を、素材In、再生速度、逆再生と素材の時間基準で変換する。表示タイムコードの開始オフセットは最後に加える。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/source_monitor.rs](../../../../crates/engine/src/source_monitor.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
