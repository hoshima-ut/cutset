# 入力色空間の設計（CO-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材のタグ・メタデータから検出した色空間を表示し、素材単位の上書きを選ぶ。変換前後の同一フレームを比較する。

## データと処理境界

検出値、手動解釈値、決定した入力変換を分け、素材IDを参照する配置に同じ解釈を適用する。原本タグは上書きしない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/color.rs](../../../../crates/engine/src/color.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>color.spaces</code> | <code>{}</code> | [color.rs](../../../../crates/engine/src/color.rs) |
| <code>media.colorInfo</code> | <code>{"item":id}</code> | [color.rs](../../../../crates/engine/src/color.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
