# 発言から粗編集の設計（ED-44）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

複数素材の発言を選び、順序を並べ替え、新規シーケンスの初稿として配置する。

## データと処理境界

発言の順序と原本ID、素材In/Out、話者、配置先を分けて記録する。前後の余白は原本参照を通して再編集できる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/transcript.rs](../../../../crates/engine/src/transcript.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
