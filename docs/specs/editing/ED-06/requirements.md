# ED-06 表示ガイド — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

色・アルファ・フィールド・セーフエリアと定規を試聴用に切り替える。

## 受入条件

半透明素材のアルファを確認して合成表示へ戻る。ガイドを保存・再読込しても出力映像に線が入らない。

## 例外と復旧

アルファなし素材やプログレッシブ素材で意味のない検査は、全不透明または対象外と明示する。

## 参照資料と確認項目

- [A088](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/set-display-options-for-interlaced-footage.html)　動体のインターレース映像を第1・第2フィールドで切り替え、異なる時刻の輪郭を個別に確認する。（公開手順）
- [A093](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/time-controls-in-the-source-and-program-monitors.html)　モニターの現在時刻を直接入力してから1フレーム送って、再生ヘッドと表示時刻が同じ量だけ進むか見る。（公開手順）
- [A094](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/view-safe-zones-in-the-monitors.html)　セーフエリアを表示してタイトル端を合わせ、非表示に戻してもタイトル座標と納品映像に影響しないか確認する。（公開手順）
- [A095](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/change-the-unit-of-measurement.html)　定規の単位を切り替え、同じ位置のガイドが新しい単位の値として読めるか照合する。（公開手順）
- [A096](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/add-or-remove-guides.html)　水平・垂直ガイドを1本ずつ作って片方を削除し、残る軸と位置を確かめる。（公開手順）
- [A097](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/snap-objects-to-guides.html)　スナップの有効時と無効時で図形をガイド付近まで動かし、最終座標と吸着表示を比較する。（公開手順）
- [A098](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/nudge-clips-in-program-monitor.html)　Programで選んだグラフィックをキーで微調整して、隣のグラフィックと拡大率が変化しないか試す。（公開手順）
- [A099](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/save-export-and-import-custom-guides.html)　縦動画用のガイドセットを書き出し、空の別案件に読み込んで本数・方向・位置を照合する。（公開手順）
