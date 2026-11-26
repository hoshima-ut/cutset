# ED-38 カメラ切替編集 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

再生中に切替キーを押してカット点を打ち、停止中は選択区間の採用アングルを切り替える。音声固定か追従かを選ぶ。

## データと処理境界

カットはシーケンス時刻と角度ID、音声経路を保存する。モニター上のタイル配列が変わっても選択した角度IDを維持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/multicam.rs](../../../../crates/engine/src/multicam.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>multicam.audioFollowsVideo</code> | <code>{"enabled":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.autoAdjustQuality</code> | <code>{"enabled":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cut</code> | <code>{"camera":1..16&#124;"angle":0-based,"time":ticks?,"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera</code> | <code>{"camera":1..16&#124;"angle":0-based,"time":ticks?,"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera1</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera2</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera3</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera4</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera5</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera6</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera7</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera8</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.cutToCamera9</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.editCameras</code> | <code>{"sequence":id?,"cameras":[{"angle":0-based,"name":str?,"enabled":bool?}]?,"audio":"camera1&#124;all&#124;switch"?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.grid</code> | <code>{"time":ticks?,"playing":bool?,"cellPixels":f32?,"playbackScale":f32?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.gridLayout</code> | <code>{"layout":"auto&#124;2x2&#124;3x3&#124;4x4"}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.inspect</code> | <code>{"time":ticks?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.nextPage</code> | <code>{}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.page</code> | <code>{"page":0-based&#124;"next"&#124;"prev"}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.prevPage</code> | <code>{}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.recordStart</code> | <code>{"time":ticks?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.recordStop</code> | <code>{"time":ticks?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera1</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera2</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera3</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera4</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera5</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera6</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera7</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera8</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectCamera9</code> | <code>{"videoOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.selectionTopDown</code> | <code>{"enabled":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.showPreviewMonitor</code> | <code>{"enabled":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.switchAngle</code> | <code>{"camera":1..16 (shown order)&#124;"angle":0-based,"clips":[id]?,"time":ticks?,"videoOnly":bool?,"audioOnly":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>multicam.transmitView</code> | <code>{"enabled":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
