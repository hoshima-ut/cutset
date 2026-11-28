# 台本とテイクの対応付けの設計（ED-60）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

台本パネルでテキストを貼り付けるか読み込んで台本を作る。行を選んでプロジェクトのクリップをドロップするとテイクが割り当たり、線の端をドラッグして範囲を変える。テイクの色、注記、サムネイルの時刻を変えられる。すべて `script.*` の編集命令で行い、取り消せる。

## データと処理境界

台本は案件の項目として保存され、行・テイク・注記を固有のIDで持つ。読込時にIDの重複と範囲外を検査し、元素材が消えたテイクは参照を外して名前を残す。

## 既存実装との対応

方針は「上流対応を要確認」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/script_commands.rs](../../../../crates/engine/src/script_commands.rs)、[crates/project/src/script.rs](../../../../crates/project/src/script.rs)、[crates/ui-egui/src/panels/script.rs](../../../../crates/ui-egui/src/panels/script.rs)。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
