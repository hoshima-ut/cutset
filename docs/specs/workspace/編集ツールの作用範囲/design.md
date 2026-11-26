# 編集ツールの作用範囲の設計（UI-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

中央、左端、隣のクリップとの境界を順に指す。選択したツールで動く端と連動トラックをドラッグ前に強調する。

## データと処理境界

ヒット位置、トリム種別、対象配置ID、ロックと素材余白からプレビューを計算し、ボタンを離した時だけ編集を確定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/tools.rs](../../../../crates/ui-egui/src/panels/tools.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
