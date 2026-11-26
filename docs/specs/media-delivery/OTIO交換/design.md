# OTIO交換の設計（IO-52）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

OTIO出力で時間軸と素材参照を確認して受け手で開き、戻りデータとの差分を照合する。

## データと処理境界

シーケンスの配置をトラック、Clip、Gap、素材参照、有理数の範囲へ変換する。エフェクト等の変換対象外は配置別に記録する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/interchange/src/otio.rs](../../../../crates/interchange/src/otio.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.exportOtio</code> | <code>{"path":str}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
