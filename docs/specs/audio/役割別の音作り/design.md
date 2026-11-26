# 役割別の音作りの設計（AU-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

対象配置を選んで会話・音楽・効果音・環境音の役割を指定し、利用可能な処理を表示する。複数選択は共通項と混在値を区別する。

## データと処理境界

役割は配置に保持し、役割固有の処理設定と共通ゲインを別に扱う。役割変更で外れる処理を確定前に列挙する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/essential_sound.rs](../../../../crates/engine/src/essential_sound.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>essentialSound.applyPreset</code> | <code>{"clips":[id]?,"preset":str,"type":"dialogue&#124;music&#124;sfx&#124;ambience"?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.autoMatch</code> | <code>{"clips":[id]?,"target":lufs?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.clearType</code> | <code>{"clips":[id]?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.deletePreset</code> | <code>{"name":str,"type":"dialogue&#124;music&#124;sfx&#124;ambience"?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.generateDucking</code> | <code>{"clips":[id]?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.inspect</code> | <code>{"clips":[id]?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.savePreset</code> | <code>{"clips":[id]?,"name":str}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.set</code> | <code>{"clips":[id]?,"key":"repair.noise.on&#124;repair.noise.amount&#124;repair.humHz&#124;clarity.eqPreset&#124;creative.reverbPreset&#124;ducking.reduceDb&#124;volume.levelDb&#124;mute&#124;…","value":any,"values":{key:value}?,"begin":bool?}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |
| <code>essentialSound.setType</code> | <code>{"clips":[id]?,"type":"dialogue&#124;music&#124;sfx&#124;ambience"}</code> | [essential_sound.rs](../../../../crates/engine/src/essential_sound.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
