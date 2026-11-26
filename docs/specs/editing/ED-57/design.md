# ED-57 検出結果の適用先 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

検出候補を選んで、素材マーカー、サブクリップ、タイムライン分割のいずれに反映するか選ぶ。

## データと処理境界

検出結果を再解析せず、素材座標から選んだ出力先の座標へ変換する。実カットは対象配置・対象トラック・リンク対象を確定してから追加する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/scene_detect.rs](../../../../crates/engine/src/scene_detect.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
