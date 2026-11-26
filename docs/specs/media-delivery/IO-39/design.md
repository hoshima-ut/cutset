# IO-39 拡張ホスト — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

拡張を追加する前に提供能力・ホスト版・必要権限を確認し、案件で不足している拡張を一覧表示する。

## データと処理境界

拡張IDと対応版、能力IDを案件の使用箇所に結び付ける。編集操作はホストのコマンド検証と権限判定を介す。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/automation/src/server.rs](../../../../crates/automation/src/server.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
