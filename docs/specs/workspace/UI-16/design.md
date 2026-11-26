# UI-16 実行環境の診断 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

診断画面で現在の素材と出力設定を指定し、読込、プレビュー、符号化に使える経路と不足条件を見る。

## データと処理境界

デマルチプレクサ、デコーダー、描画、エンコーダー、保存先の空き容量を段階ごとに評価し、実測と未確認を区別する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/menu_dialogs.rs](../../../../crates/ui-egui/src/panels/menu_dialogs.rs)。

確認した関数：[system_report](../../../../crates/ui-egui/src/panels/menu_dialogs.rs)。エンジンの診断結果にGPU名・バックエンド・ドライバーを追加し、CPU描画時も識別する。端末別の全デコード能力と素材ごとの実経路は別途検証する。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>help.systemReport</code> | <code>{}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>perf.stats</code> | <code>{}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
