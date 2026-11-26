# ED-06 表示ガイド — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

モニターの表示を合成、アルファ、個別成分へ切り替え、ルーラー・ガイド・セーフエリアを重ねて確認する。

## データと処理境界

表示切替は素材・完成の各モニターに保持する。合成後の納品画像への画素処理とは別の表示段階でガイドを描く。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/monitor.rs](../../../../crates/ui-egui/src/panels/monitor.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
