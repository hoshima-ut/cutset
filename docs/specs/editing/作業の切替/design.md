# 作業の切替の設計（ED-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材準備で対象案件を選び、編集でシーケンスを開き、納品設定の確認後に編集へ戻る。

## データと処理境界

各作業面が共有するのは案件IDと現在のシーケンスID。パネル構成、素材側の位置、出力範囲の仮入力は作業面ごとに保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/import_mode.rs](../../../../crates/ui-egui/src/panels/import_mode.rs)、[apps/filmcraft/src/main.rs](../../../../apps/filmcraft/src/main.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。

<a id="premiere-27-1"></a>

## 編集からカラーへ切り替える（27.0との照合）

選択配置、再生フレーム、再生範囲を保ってカラー作業面へ移る。補正は同じ配置の効果履歴に保存する。
