# 映像スコープの設計（CO-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

調べるフレームと信号の段階を選び、波形・パレード・ベクトル・ヒストグラムを並べる。信号空間・レンジ・単位を表示する。

## データと処理境界

同じフレームの成分値から各スコープを計算する。プローブ対象が表示変換前か後かを記録し、HDRは線形値・コード値・輝度表示を区別する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/scopes.rs](../../../../crates/engine/src/scopes.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>scopes.read</code> | <code>{"scopes":["waveform","parade","histogram","vectorscopeYuv","vectorscopeHls"]?,"waveformType":"rgb&#124;luma&#124;yc&#124;ycNoChroma"?,"paradeType":"rgb&#124;yuv&#124;rgbWhite"?,"colorSpace":"auto&#124;601&#124;709&#124;2100"?,"clamp":bool=true,"columns":n=8,"peaks":n=8,"bins":bool=true,"scale":0.5,"time":ticks?&#124;"frame"&#124;"seconds"&#124;"timecode"}</code> | [scopes.rs](../../../../crates/engine/src/scopes.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
