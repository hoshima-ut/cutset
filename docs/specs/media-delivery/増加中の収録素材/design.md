# 増加中の収録素材の設計（IO-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

収録中として開き、更新時に読み取れる末尾を伸ばす。既存の選択や配置を維持したまま新しい区間を試聴する。

## データと処理境界

ファイルサイズの増分と確定したパケットを走査し、映像・音声が実際に読める範囲を返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/media_watch.rs](../../../../crates/engine/src/media_watch.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
