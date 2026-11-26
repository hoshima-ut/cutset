# ED-37 複数カメラの同期 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

カメラ素材と外録音を選び、タイムコード、指定マーカー、音声のどれで合わせるか選び、結果のオフセットを確認する。

## データと処理境界

角度IDごとに原本IDと共通時刻軸へのオフセットを持たせる。重複名の識別は表示名だけに依存しない。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/multicam.rs](../../../../crates/engine/src/multicam.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.createMulticam</code> | <code>{"items":[id]?,"name":str?,"method":"in&#124;out&#124;timecode&#124;marker&#124;audio","ignoreHours":bool?,"marker":str?,"offset":frames?,"audio":"camera1&#124;all&#124;switch","cameraNames":"clip&#124;track&#124;metadata","processedBin":bool?,"reference":item?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>clip.mergeClips</code> | <code>{"items":[id]?,"method":"in&#124;out&#124;timecode&#124;marker&#124;audio","name":str?,"removeVideoAudio":bool?,"ignoreHours":bool?,"marker":str?,"offset":frames?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>clip.multicamEnable</code> | <code>{"clips":[id]?,"enabled":bool?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>clip.multicamFlatten</code> | <code>{"clips":[id]?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |
| <code>clip.synchronize</code> | <code>{"method":"in&#124;out&#124;timecode&#124;marker&#124;audio","clips":[id]?,"reference":clip?,"track":"V1"&#124;"A1"?,"ignoreHours":bool?,"marker":str?,"offset":frames?}</code> | [multicam.rs](../../../../crates/engine/src/multicam.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
