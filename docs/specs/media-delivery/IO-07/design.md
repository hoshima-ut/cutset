# IO-07 静止画・連番 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

番号付き画像の先頭を選び、単体または連番、再生レートと欠番の扱いを選択する。

## データと処理境界

同じディレクトリ、名前パターン、桁幅で候補を抽出し、数値順に並べる。各番号と素材フレームの対応を保存する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/media/src/sequence.rs](../../../../crates/media/src/sequence.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.importImageSequence</code> | <code>{"path":str,"bin":binId?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
