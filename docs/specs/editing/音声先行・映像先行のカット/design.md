# 音声先行・映像先行のカットの設計（ED-31）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

リンクした映像音声の片側の編集点だけを選び、前の音と次の音・画の重なりを試聴する。

## データと処理境界

音声の素材点と配置点を同量動かし、映像の素材・配置時刻対応を固定する。リンク関係と参照する共通素材時刻は保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/split_edit_ripple_trim_tests.rs](../../../../crates/engine/src/split_edit_ripple_trim_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
