# 速度・逆再生の設計（ED-33）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

配置の速度、逆向き、音程保持、後続のリップルを指定し、見込まれる尺を確認する。

## データと処理境界

再生率と素材範囲から新しい配置長を算出し、映像サンプリングと音声の伸縮設定を個別に渡す。後続移動はオプションで決める。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/linked_speed_tests.rs](../../../../crates/engine/src/linked_speed_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.setTimeInterpolation</code> | <code>{"clips":[id]?,"mode":"frameSampling&#124;frameBlending&#124;opticalFlow"}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.speedDuration</code> | <code>{"clips":[id]?,"speed":percent=100,"reverse":bool,"ripple":bool,"maintainPitch":bool? (Maintain Audio Pitch; unchanged when left out),"interpolation":"frameSampling&#124;frameBlending&#124;opticalFlow"?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>clip.timeInterpolation.frameBlending</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.timeInterpolation.frameSampling</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.timeInterpolation.opticalFlow</code> | <code>{"clips":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>timeline.rateStretch</code> | <code>{"clip":id,"edge":"in&#124;out","delta":ticks,"linked":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
