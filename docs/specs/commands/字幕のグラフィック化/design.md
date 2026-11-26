# 字幕のグラフィック化の設計（MN-20）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象字幕キューを選択し、変換後のグラフィックのトラックと字幕納品への影響を確認して確定する。

## データと処理境界

キューの文字、時刻、表示スタイルをタイトル配置へ写し、変換したキューと新配置の対応を保持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs)。

確認した関数：[upgrade_caption](../../../../crates/engine/src/graphic_templates.rs)。字幕をグラフィックへ変換し、字幕項目が減る挙動を試験している。納品サイドカーからの除外と日本語表示の一致は別途照合する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
