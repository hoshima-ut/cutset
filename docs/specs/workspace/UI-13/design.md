# UI-13 キーボードと支援技術 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

キーボードでタイムライン、編集点、字幕入力欄へ移動する。編集後は直前の一覧行にフォーカスを戻す。

## データと処理境界

支援技術へ対象部品の役割・名前・状態・時刻・選択数を伝える。トリム量と字幕本文はキーで数値・文字入力できる。

## 既存実装との対応

方針は「上流対応を要確認」。対象マイルストーンは[M1](../../../development/milestones.md)。

上流コードの照合先：[crates/ui-egui/src/panels/tools.rs](../../../../crates/ui-egui/src/panels/tools.rs)。

確認した関数：[show](../../../../crates/ui-egui/src/panels/tools.rs)。ツール選択パネルのTab移動・フォーカス枠・Spaceによる選択にUI試験がある。トリムから字幕訂正までの読み上げはこの試験の対象外。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
