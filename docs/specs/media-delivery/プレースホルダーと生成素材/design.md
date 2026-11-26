# プレースホルダーと生成素材の設計（IO-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

生成素材の種類・寸法・尺を指定してビンに追加する。仮素材は後から原本に再リンクする。

## データと処理境界

黒、透明、色面、基準信号、欠落素材の種類を保持する。参照先を変えても配置の識別子とタイムライン範囲を維持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/media/src/generators.rs](../../../../crates/media/src/generators.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.newBarsAndTone</code> | <code>{"seconds":f64=10,"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newBlackVideo</code> | <code>{"seconds":f64,"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newColorMatte</code> | <code>{"color":"#rrggbb"?,"seconds":f64=5,"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newCountingLeader</code> | <code>{"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.newOfflineFile</code> | <code>{"name":str?,"fileName":str?,"tapeName":str?,"video":bool=true,"audio":bool=true,"width":u32?,"height":u32?,"fps":f64?,"sampleRate":u32=48000,"channels":u32=2,"timecode":"HH:MM:SS:FF"?,"seconds":f64=10,"description":str?}</code> | [clip_ops.rs](../../../../crates/engine/src/clip_ops.rs) |
| <code>file.newTransparentVideo</code> | <code>{"bin":binId?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
