# 入力チャンネル割当の設計（AU-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材のチャンネルを個別試聴し、入力と配置上のモノ・ステレオ・多チャンネルの対応表を編集する。適用範囲を確認してからミキサーで出力を試す。

## データと処理境界

入力のチャンネル数と順序、出力レイアウト、各経路の係数を保持する。素材解釈・配置・出力バスの各段で実効経路を取得できる。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/audio-dsp/src/channels.rs](../../../../crates/audio-dsp/src/channels.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>clip.audioChannels</code> | <code>{"items":[id]?,"format":"mono&#124;stereo&#124;5.1&#124;adaptive","clips":[[channel]]?,"channels":[channel]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.breakoutToMono</code> | <code>{"items":[id]?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>clip.extractAudio</code> | <code>{"items":[id]?,"dir":str?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
