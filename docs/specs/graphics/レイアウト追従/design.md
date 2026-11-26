# レイアウト追従の設計（GR-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

背景図形の端と文字枠を関連付け、入場と退場の保護区間を指定する。文字列と配置尺を変え、帯の余白とアニメ速度を確認する。

## データと処理境界

空間のピンは参照レイヤーID・辺・余白、時間の保護は開始端・終了端からの長さで保存する。尺の差は保護外の区間へ配分する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs)。

確認した関数：[pin_layer](../../../../crates/engine/src/graphic_templates.rs)。レイヤーを画面または他レイヤーに固定し、テキストの伸びへの追従を扱う。未導入フォントや複数の出力比率での配布結果を別途評価する。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>graphics.pin</code> | <code>{"clip":id?,"layer":n&#124;name?,"to":"frame"&#124;"none"&#124;layer index&#124;layer name,"edges":["left","top","right","bottom"]&#124;"all"="all"}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.setResponsiveTime</code> | <code>{"clip":id?,"introFrames":n?,"outroFrames":n? (or introSeconds / outroSeconds, or ticks as intro / outro)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |
| <code>graphics.setRoll</code> | <code>{"clip":id?,"mode":"off&#124;roll&#124;crawlLeft&#124;crawlRight"?,"startOffScreen":bool?,"endOffScreen":bool?,"prerollFrames":n?,"easeInFrames":n?,"easeOutFrames":n?,"postrollFrames":n? (or …Seconds, or ticks as preroll/easeIn/easeOut/postroll)}</code> | [graphic_templates.rs](../../../../crates/engine/src/graphic_templates.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
