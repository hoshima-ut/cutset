# UI-10 試聴品質 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

再生中と停止時の品質を独立指定し、表示倍率やドロップ数を確認する。

## 受入条件

再生品質と停止品質を切り替え、コマ落ち表示、外部モニターと内部出力を確認する。プレビューを軽くしてもレンダー済みファイルの品質は指定値を守る。

## 例外と復旧

外部表示が切断されたら内部表示を継続し、外部のみで利用可能だった設定を無効と表示する。

## 参照資料と確認項目

- [A036](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/playback-preferences.html)　外部再生の有無を変え、映像と音声の送り先が設定どおりに切り替わる。（公開手順）
- [A083](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/set-display-quality-for-the-source-and-program-monitors.html)　再生時だけプレビュー解像度を下げ、停止画の設定と最終書き出し寸法が維持されるか試す。（公開手順）
- [A084](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/adjust-the-magnification-for-the-source-and-program-monitors.html)　両モニターを異なる倍率にして同じテロップの縁を拡大し、タイムライン上のScale値に変更がないか確認する。（公開手順）
- [A085](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/enable-high-quality-playback.html)　高品質再生を切り替えて縮小時の細線の見え方とコマ落ち数を記録し、編集点が動かないことを照合する。（公開手順）
- [A086](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/choose-a-display-mode.html)　RGBAの各単色表示と合成表示で既知の半透明素材を表示し、アルファの白黒が実際の透明度に対応するか確かめる。（公開手順）
- [A100](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/enable-dropped-frame-indicator.html)　コマ落ち表示を有効にして高負荷素材とプロキシを順に再生し、カウンターと実際の再生条件を記録する。（公開手順）
- [A779](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/timeline-doesnt-show-video-preview.html)　プレビュー非表示時にソース単体とシーケンスを分けて再生し、問題箇所を絞る。（障害診断）
- [A780](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/not-able-to-optimize-playback-performance.html)　同じ区間の再生解像度とプロキシを変え、コマ落ちと復旧の条件を計測する。（障害診断）
- [A785](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/choppy-playback-and-poor-performance-issue.html)　コマ落ちした箇所を記録してレンダー出力と照合し、プレビュー限定の異常を特定する。（障害診断）
- [A786](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/slow-rendering-and-playback.html)　同一区間のキャッシュ有無でレンダー時間とリアルタイム再生を別々に測る。（障害診断）
