# UI-19 HDRの監視 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材・作業・出力・ディスプレイの色空間を表示し、現在の表示経路を確認する。

## 受入条件

OSのHDR表示、入力素材・作業・出力の色空間、モニター能力を別に表示。対応／非対応ディスプレイで同じチャートを比較し、表示差を出力データの変更と取り違えない。

## 例外と復旧

HDRに対応しない画面ではSDRへのプレビュー変換を明示し、HDR出力が実機確認済みと表示しない。

## 参照資料と確認項目

- [A053](https://helpx.adobe.com/premiere/desktop/get-started/set-up-directx-hdr-for-windows/supported-operating-systems-gpus-and-displays-for-directx-hdr-support.html)　OS・GPU・表示器のうち一つだけ欠く組合せでHDR表示の可否を確かめる。（公開手順）
- [A054](https://helpx.adobe.com/premiere/desktop/get-started/set-up-directx-hdr-for-windows/set-up-your-system-for-directx-hdr.html)　Windows側のHDR設定前後を既知のチャートで比べ、表示器の状態を記録する。（公開手順）
- [A055](https://helpx.adobe.com/premiere/desktop/get-started/set-up-directx-hdr-for-windows/supported-and-unsupported-features-with-directx-hdr-and-premiere.html)　DirectX HDRでサポートされる表示先と対象外の表示先を同じ案件で比べる。（公開手順）
- [A056](https://helpx.adobe.com/premiere/desktop/get-started/set-up-directx-hdr-for-windows/set-up-premiere-for-directx-hdr.html)　OS設定の後にアプリ側で表示を切り替え、二重の色変換が起きないか確認する。（公開手順）
