# フレームと連番出力の設計（IO-47）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象モニターと時刻、または範囲と採番規則を選び、出力名をプレビューして保存する。

## データと処理境界

シーケンスと素材の時刻を区別し、連番では実フレーム数と番号の開始・桁数、アルファ、色変換を固定する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/frame_export_tests.rs](../../../../crates/engine/src/frame_export_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportFrame</code> | <code>{"path":str?,"format":"png&#124;jpeg&#124;tiff&#124;bmp"?,"depth":8&#124;16?,"import":bool?,"target":"source&#124;program"?,"item":id?,"sequence":id?,"time":ticks?}</code> | [keyboard.rs](../../../../crates/engine/src/keyboard.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
