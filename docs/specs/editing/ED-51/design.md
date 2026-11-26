# ED-51 受け渡し用の展開 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

カメラ割りを保持した元シーケンスを選び、展開、不要行の除外、素材余白の扱いを指定して受け渡し用コピーを作る。

## データと処理境界

出力には元シーケンスIDとコピーID、各配置の原本範囲、焼込み・省略した要素を記録する。元の角度選択とリンクを維持する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M4](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/nest_fidelity_tests.rs](../../../../crates/engine/src/nest_fidelity_tests.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>sequence.simplify</code> | <code>{"name":str?,"removeDisabled":bool=true,"removeEmptyTracks":bool=true,"closeGaps":bool=false,"moveClipsDown":bool=false,"removeVideoEffects":bool=false,"removeAudioEffects":bool=false,"removeText":bool=false,"keep":"both&#124;video&#124;audio"?}</code> | [sequence_extras.rs](../../../../crates/engine/src/sequence_extras.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
