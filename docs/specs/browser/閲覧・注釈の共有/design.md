# 閲覧・注釈の共有の設計（WB-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

共有する案件版、再生範囲、試聴用素材を選び、閲覧・注釈と有効期限を確認して共有する。受け手には版と権限を明示する。

## データと処理境界

共有対象は確定版から生成した参照用メディア・時間対応とアクセス権を持つ。配信側は各取得・注釈要求で有効期限と権限を検査する。

## 既存実装との対応

方針は「新規設計」。対象マイルストーンは[M6](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/export_tools.rs](../../../../crates/engine/src/export_tools.rs)。

確認した関数：[settings_from_params](../../../../crates/engine/src/export_tools.rs)。試聴用メディア生成の土台として書き出し設定を解決できる。版の固定、共有URL、閲覧・注釈権限、有効期限を管理する配信側は新規設計。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
