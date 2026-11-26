# IO-26 試聴と納品の素材選択 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

試聴用の代理を切り替え、書き出し画面では納品に使う原本・代理を確認する。

## データと処理境界

再生用選択と出力ジョブの素材選択を独立させ、ジョブには各素材で採用する参照先を記録する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/proxies.rs](../../../../crates/engine/src/proxies.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
