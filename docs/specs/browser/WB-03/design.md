# WB-03 ネイティブとWasmの編集整合 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

案件を開く際にブラウザーとネイティブの利用可能能力を表示する。同じ編集操作は共通命令で実行し、対応できないメディアは代理表示を選ぶ。

## データと処理境界

時間・配置・Undoを共通の決定的な編集モデルで処理する。デコード、ファイル、描画デバイスはホスト能力を照会し、整数時刻を境界で暗黙に浮動小数点へ丸めない。

## 既存実装との対応

方針は「既存部品を拡張」。対象マイルストーンは[M6](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/wasm_clock_tests.rs](../../../../crates/engine/src/wasm_clock_tests.rs)、[apps/filmcraft-web/src/lib.rs](../../../../apps/filmcraft-web/src/lib.rs)。

確認した関数：[start](../../../../apps/filmcraft-web/src/lib.rs)。ブラウザーの起動時にWebServicesを注入して共通エンジンのSessionを作成する。機能ごとのホスト能力とフレーム・サンプル単位の同値性をネイティブと照合する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
