# GR-05 再利用するスタイル — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

共有スタイルを選んで複数テロップへ適用し、一箇所だけ色を上書きする。共有設定を更新すると影響する配置を一覧で確認できる。

## データと処理境界

スタイル参照と属性ごとの上書き値を別々に保持する。実効値は共有値へ個別属性を重ねて求め、字幕とタイトルで非対応属性を区別する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphics.rs](../../../../crates/engine/src/graphics.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>graphics.align</code> | <code>{"clip":id?,"layers":[n]?,"align":"left&#124;hcenter&#124;right&#124;top&#124;vcenter&#124;bottom","to":"frame&#124;group&#124;selection"="frame" (frame: each layer; group: the layers' union; one layer always aligns to the frame)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignFrame.bottom</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignFrame.hcenter</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignFrame.left</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignFrame.right</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignFrame.top</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignFrame.vcenter</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignGroup.bottom</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignGroup.hcenter</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignGroup.left</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignGroup.right</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignGroup.top</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignGroup.vcenter</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignSelection.bottom</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignSelection.hcenter</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignSelection.left</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignSelection.right</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignSelection.top</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.alignSelection.vcenter</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.bringForward</code> | <code>{"clip":id?,"layer":n?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.bringToFront</code> | <code>{"clip":id?,"layer":n?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.distribute</code> | <code>{"clip":id?,"layers":[n] (3 or more)?,"axis":"horizontal&#124;vertical","space":bool=false (equal gaps instead of equal centre spacing)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.distributeHorizontally</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.distributeSpaceHorizontally</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.distributeSpaceVertically</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.distributeVertically</code> | <code>{"clip":id?,"layers":[n]? (default: the selected layers; selected video clips move by Motion Position)}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.sendBackward</code> | <code>{"clip":id?,"layer":n?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |
| <code>graphics.sendToBack</code> | <code>{"clip":id?,"layer":n?}</code> | [graphics.rs](../../../../crates/engine/src/graphics.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
