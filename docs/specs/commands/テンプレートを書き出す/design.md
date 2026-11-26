# テンプレートを書き出すの設計（MN-21）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

単一のタイトルを選び、外部に公開する文字・色・差し替え素材の項目と依存一覧を確かめてひな型を作る。

## データと処理境界

ひな型に版、公開属性の型・既定値、依存素材の参照を記録する。複数選択時は対応する対象を明示する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
