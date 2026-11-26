# UX-03 同期テイクからの差し替え — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

同期済みカメラ群と外録音を開き、映像だけを別角度にする範囲を選び、切替前後を聴いて確定する。

## データと処理境界

外録音の配置IDと時刻を固定したまま、選択した映像区間を共通同期時刻から次の角度の素材点へ変換する。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/multicam.rs](../../../../crates/engine/src/multicam.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
