# MN-17 トラックの一括変更 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

トラックの種別、基準行、追加位置と本数を指定する。削除では空のみ・指定行と影響する配置数を確認する。

## データと処理境界

操作時には表示番号をトラックIDへ解決する。トラック削除とビン内素材の削除を分離し、既存IDを並べ替えで再利用しない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/sequence_tools.rs](../../../../crates/engine/src/sequence_tools.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
