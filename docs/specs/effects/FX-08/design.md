# FX-08 変形とアンカー — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

画面でアンカーを選んで移動し、数値欄で角度と倍率を入力する。縦横比ロックの状態はドラッグでも数値変更でも共通に扱う。

## データと処理境界

素材座標のアンカーとシーケンス座標の位置を区別し、アンカーを中心に拡大縮小・回転を合成する。UIとレンダーは同じ変換値を読む。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/transform_handles.rs](../../../../crates/ui-egui/src/panels/transform_handles.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.fillFrame</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.fitToFrame</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.scaleToFrameSize</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
