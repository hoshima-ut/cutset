# 素材横断の発言検索の設計（UX-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象ビン・話者を選んで発言を検索し、候補の前後を元音で確認して使用する行を選ぶ。

## データと処理境界

検索結果は原本ID、語の開始・終端、話者IDを返し、同じ語の別出現を別行にする。表示用の表記と原音位置を同期させる。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M3](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/transcript.rs](../../../../crates/engine/src/transcript.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
