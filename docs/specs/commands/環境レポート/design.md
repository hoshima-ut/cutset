# 環境レポートの設計（MN-28）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

ヘルプから診断を開き、OS、入出力機器、描画経路などを確認する。共有する項目を選びローカルに保存する。

## データと処理境界

診断は案件がなくても動作し、項目ごとの取得可否を返す。ファイルパス、接続資格情報、案件中の素材情報はレポートへ無条件に含めない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/project_tools.rs](../../../../crates/engine/src/project_tools.rs)。

確認した関数：[system_report](../../../../crates/engine/src/project_tools.rs)。OS・ビルドと書き出し形式の可否を返す。GUIで共有項目を選んだ場合の保存内容と個人情報の除外は別途確認する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
