# UI-16 実行環境の診断 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

端末の能力と選択素材に応じて再生・書き出し経路を説明する。

## 受入条件

OS、デバイス、ドライバー、素材形式による読込・再生・書出しの可否を別々に報告する。空き容量不足時に既存の書出しと最後の保存版を保護する。

## 例外と復旧

GPUが利用不能なら利用可能なCPU経路と影響を表示する。いずれも使えない操作は入力条件を添えて停止する。

## 参照資料と確認項目

- [A001](https://helpx.adobe.com/premiere/desktop/whats-new/whats-new.html)　新機能一覧の項目から対象ビルドに移動でき、正式・先行公開の区別が付く。（版横断の公式情報。26.xの見出しだけを対象とする）
- [A002](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html)　不具合の再現案件に修正版番号を添え、修正前後の結果を別々に記録する。（版横断の公式情報。26.xの見出しだけを対象とする）
- [A003](https://helpx.adobe.com/premiere/desktop/whats-new/beta-features.html)　ベータ専用の操作を正式版の受入件数から除き、比較用に版と日付を残す。（公開ベータの総覧。26.x正式機能の根拠にしない）
- [A004](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-pro-technical-requirements.html)　現在版と26系で必要環境が異なる場合に、26系の試験端末を現在版の条件で除外しない。（現行要件は版混在。26.xの対象機器はID 16で照合）
- [A005](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/gpu-and-gpu-driver-requirements.html)　同じ素材を異なるドライバーで開き、GPUの識別と利用可否を診断記録に残す。（版混在。GPUメモリ不足で起動不可とする新しい最低基準は27.0）
- [A006](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/storage-recommendations.html)　原本、キャッシュ、書き出し先を分け、残容量不足がどの作業を止めたか示す。（公開手順）
- [A007](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/processor-memory-and-gpu-recommendations.html)　代表CPU・メモリ量で同じ尺を再生し、ボトルネックを対比できる。（公開手順）
- [A014](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-25x-technical-requirements.html)　旧25系端末の条件を26系要件の欄に混在させない。（25.x専用。旧版比較）
- [A015](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-24x-technical-requirements.html)　旧24系の動作報告から26系でも起動できると誤判定しない。（24.x専用。旧版比較）
- [A016](https://helpx.adobe.com/premiere/desktop/get-started/technical-requirements/adobe-premiere-26x-technical-requirements.html)　OS・CPU・GPUを26系の要求値で照合し、試験対象ビルドと組で記録する。（26.x専用の公式動作要件）
- [A017](https://helpx.adobe.com/premiere/desktop/get-started/download-and-install/creative-cloud-apps-available-for-download.html)　インストール候補に対象版があるか確認し、利用可能な配布版を明示する。（公開手順）
- [A018](https://helpx.adobe.com/premiere/desktop/get-started/download-and-install/best-practices-for-updating-premiere.html)　更新前に保管した案件コピーで旧プラグイン、保存、書き出しの結果を比較する。（公開手順）
- [A019](https://helpx.adobe.com/premiere/desktop/get-started/download-and-install/check-if-your-system-is-compatible-with-premiere.html)　端末互換性レポートから問題のある機器を特定し、案件エラーと分ける。（版混在。GPUメモリ不足で起動不可とする新しい最低基準は27.0）
- [A020](https://helpx.adobe.com/premiere/desktop/get-started/download-and-install/mercury-playback-engine-gpu-accelerated-in-premiere.html)　GPU対象の効果とCPU処理の区間を含むシーケンスでプレビュー結果を照合する。（25.2以降のソフトウェアのみのレンダラー廃止を継承。書き出し時のソフトウェアエンコードと別）
- [A739](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/known-and-fixed-issues.html)　既知・修正済みの事例に再現素材と対象ビルドを添え、再発を別件として識別する。（障害診断）
- [A758](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/fix-outdated-windows-libraries.html)　起動依存ライブラリが不足したWindows環境で、診断に不足部品を記録する。（障害診断）
- [A760](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/no-splash-screen-appears-on-app-launch.html)　スプラッシュ表示前に終了するケースでインストール・依存関係の診断へ到達する。（障害診断）
- [A761](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/try-adobe-creative-cloud-diagnostics.html)　診断情報を出力する前に対象ログを選べ、個別案件の内容と区別できる。（障害診断）
- [A762](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/premiere-crashes-when-you-open-a-specific-project.html)　一案件だけでクラッシュしたとき、新規案件と回復版で再現範囲を狭める。（障害診断）
- [A763](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/premiere-hangs-on-launch-on-macos.html)　macOSで起動が停止する状態を設定・拡張・端末の各条件に切り分ける。（障害診断）
- [A764](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/premiere-freezes-on-the-splash-screen.html)　起動画面で止まる読み込み段階を表示し、最後に試した拡張を特定する。（障害診断）
- [A765](https://helpx.adobe.com/premiere/desktop/troubleshooting/crash-issues/fix-premiere-crash-issues.html)　クラッシュの再現手順にビルド・素材・最後の操作を記録し、復旧できた版を残す。（障害診断）
