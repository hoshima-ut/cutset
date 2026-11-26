# ローカル保存と同期の設計（WB-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

作業状態を端末保存・送信待ち・同期済みに分けて表示する。タブを閉じる前に未同期件数を確認でき、再開時は保存済み編集から再送する。

## データと処理境界

編集操作ログ・素材参照・同期済み版と、再生成可能なプレビューを分ける。永続化成功後に端末保存済み、サーバー応答後に同期済みとする。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M6](../../../development/milestones.md)。

上流コードの照合先：[apps/filmcraft-web/src/opfs.rs](../../../../apps/filmcraft-web/src/opfs.rs)、[apps/filmcraft-web/src/recovery_policy.rs](../../../../apps/filmcraft-web/src/recovery_policy.rs)。

確認した関数：[written](../../../../apps/filmcraft-web/src/recovery_policy.rs)。OPFSへの復旧スナップショット書込結果を受け取り、現行版の書き込み失敗時は再試行できる状態にする。クラウド確認応答や送信待ちの操作ログは別に実装する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
