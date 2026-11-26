# 納品の音声割当の設計（AU-18）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

納品時のチャンネルレイアウト、順序、サンプルレートを指定する。原本に合わせる選択では採用予定値とバスの対応表を確定前に示す。

## データと処理境界

各入力から出力への係数と割当、リサンプルの入出力レートを記録する。多チャンネル順序はチャンネル名により対応付ける。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/export/src/surround_tests.rs](../../../../crates/export/src/surround_tests.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
