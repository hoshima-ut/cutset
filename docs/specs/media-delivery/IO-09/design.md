# IO-09 音声の取り込み — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

音声のチャンネル数と原本レートを確認して取り込み、シーケンスのレートで試聴する。

## データと処理境界

原本サンプル位置とシーケンス時間を独立して保持する。リサンプル済みキャッシュは元素材・変換条件にひも付ける。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/audio-dsp/src/resample.rs](../../../../crates/audio-dsp/src/resample.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
