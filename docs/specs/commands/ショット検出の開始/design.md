# ショット検出の開始の設計（MN-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

映像素材を選び、検出方法と、マーカー・サブクリップ・実分割のどの結果を作るかを先に決める。

## データと処理境界

検出器は素材時刻の候補境界を返す。確定時に選択した結果形式へ変換し、実分割時だけ配置範囲とリンクを扱う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/scene_detect.rs](../../../../crates/engine/src/scene_detect.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
