# AU-03 サンプル単位の編集 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

時間表示を音声サンプルに切り替え、波形を拡大して端を指定する。リンクされた映像の編集点も示し、音声だけを調整できる。

## データと処理境界

音声端は整数サンプル位置または正確に変換可能な時間単位で保持する。表示をフレームに戻しても保存値をフレーム単位へ丸めない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/timeline_volume.rs](../../../../crates/ui-egui/src/panels/timeline_volume.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
