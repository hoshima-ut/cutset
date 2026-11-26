# レイヤー画像の設計（IO-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

レイヤー画像を選び、統合・個別レイヤー・配置付きの読み込みから対応方法を選ぶ。

## データと処理境界

原寸のキャンバス、レイヤー順、原点、境界、アルファを保持し、統合時は合成結果、個別時は各素材と配置を返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/media/src/still/psd.rs](../../../../crates/media/src/still/psd.rs)。

確認した関数：[decode](../../../../crates/media/src/still/psd.rs)。PSDの統合画像を読み、合成アルファを扱う。レイヤー個別取り込みはこのデコーダーに含まれない。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
