# 編集命令の共通化の設計（UX-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

同じ配置を選び、マウス、キー、CLI、AI候補の採用、拡張から同一のトリム要求を発行する。

## データと処理境界

各入口で基準版・配置ID・端・時間差を共通命令へ変換する。操作結果として実差分・影響ID・Undo単位を返す。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/automation/src/server.rs](../../../../crates/automation/src/server.rs)、[crates/engine/src/lib.rs](../../../../crates/engine/src/lib.rs)。

確認した関数：[execute](../../../../crates/engine/src/lib.rs)。命令IDとJSON引数を受ける既存の共通入口があり、配置IDを明示すれば画面選択なしでも対象を指定できる。AI・外部拡張・GUIが同一入力で同じ結果になる横断試験は追加対象。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
