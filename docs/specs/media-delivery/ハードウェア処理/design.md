# ハードウェア処理の設計（IO-27）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

素材情報と端末能力から利用可能な処理経路を確認し、再生・出力時の実使用経路を表示する。

## データと処理境界

コンテナ、コーデック、プロファイル、色差形式、ビット深度を照合し、復号・描画・符号化を別々に選択する。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/platform/src/lib.rs](../../../../crates/platform/src/lib.rs)。

確認した関数：[hardware_decoder_for](../../../../crates/platform/src/lib.rs)。映像サンプルの記述に対応するハードウェア復号経路を問い合わせる。描画・符号化・実測性能の表示は個別に確認する。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。

<a id="premiere-27-10"></a>

## Windows ARMでのGPU・AI処理（27.0との照合）

CPUアーキテクチャ、GPU、ドライバー、推論バックエンドを操作単位で判定する。RTX Spark（N1X）とTensorRTは実機の検証対象とし、利用できる代替経路を示す。
