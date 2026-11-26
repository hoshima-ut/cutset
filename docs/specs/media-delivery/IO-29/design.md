# IO-29 キャッシュ管理 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

種類ごとのキャッシュ使用量と利用中の案件を表示し、削除対象と解放見込みを確認する。

## データと処理境界

原本、案件、自動保存と再生成可能なキャッシュを区別する。削除結果は対象件数・実際の解放量・利用中で残した件数を返す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/perf.rs](../../../../crates/engine/src/perf.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>mediaCache.clean</code> | <code>{"all":bool?}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |
| <code>mediaCache.info</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/settings/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
