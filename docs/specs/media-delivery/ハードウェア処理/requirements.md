# ハードウェア処理の要件（IO-27）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材と機器に応じたデコード・描画・エンコード経路とフォールバックを表示する。

## 受入条件

H.264/HEVCの8-bitと10-bit 4:2:2をCPU/GPU別に再生・出力し、対応表示、画の破綻、コマ落ちを記録。

## 例外と復旧

機器が受け付けない形式は利用可能な代替経路とその理由を示す。GPU指定だけを根拠に全処理をGPU使用と表示しない。

## 参照資料と確認項目

- [A008](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/hardware-accelerated-decoding-and-encoding.html)　エンコードとデコードを独立に切り替え、速さと読み戻したフレームを比較する。（版混在。26.5のBlackwell向けAVC/HEVC 4:2:2 10-bit MXFと27.0のWindows ARM拡張を区別）
- [A009](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/enable-hardware-accelerated-decoding-support.html)　ハードウェアデコードを変更し、再起動が必要なら案内したうえで適用状態を確認する。（公開手順）
- [A010](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/supported-codecs-and-drivers-for-hardware-accelerated-decoding.html)　同じ拡張子でプロファイルや色差形式が異なる素材を使い、実際のデコーダーを識別する。（版混在。26.5のBlackwell向けAVC/HEVC 4:2:2 10-bit MXFと27.0のWindows ARM拡張を区別）
- [A011](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/enable-hardware-encoding-support.html)　書き出し設定でハードウェア符号化を選び、対象外の構成で選べない理由を表示する。（公開手順）
- [A012](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/install-macos-updates-for-apple-metal-gpu-acceleration.html)　Metalの利用可否をOS版にひも付け、更新が必要な端末でも案件の所在を確認できる。（26.0はmacOS Sonoma 14が最低要件。端末・OSは26.x要件で照合）
- [A013](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/enable-mercury-playback-engine-gpu-accelerated-renderer.html)　GPUレンダラーの選択結果とエンコード方式を別々に記録する。（25.2以降のソフトウェアのみのレンダラー廃止を継承。書き出し時のソフトウェアエンコードと別）
- [A743](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/software-rendering-update.html)　GPUのない状態で利用可能なレンダー経路と選べないモードをビルド別に記録する。（25.2以降でSoftware Onlyレンダラーを廃止。26系にも継続）
- [A749](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/common-issues-in-premiere-on-apple-silicon-macs.html)　Apple Siliconの端末でネイティブ部品と外部拡張の障害を切り分ける。（障害診断）
- [A781](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/hardware-setup-not-optimal-for-playback-performance.html)　ディスク、GPU、音声機器の構成を記録し、機器交換前後を同じ区間で比較する。（障害診断）
- [A783](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/optimize-playback-performance-for-h264-h265-media.html)　H.264とHEVCで同じ内容を再生し、デコード方式とシーク応答を別々に記録する。（障害診断）

<a id="premiere-27-10"></a>

## Windows ARMでのGPU・AI処理（27.0との照合）

CPUアーキテクチャ、GPU、ドライバー、推論バックエンドを操作単位で判定する。[Adobeの公開資料](https://helpx.adobe.com/jp/x-productkb/multi/windows-arm-support.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-10)と[受入試験](tasks.md#premiere-27-10)に記載する。
