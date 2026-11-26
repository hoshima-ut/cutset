# FX-06 キーフレームの操作 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

値の時間変化を有効化し、キーの作成・移動・選択・削除・複製を行う。

## 受入条件

一つのキーを1フレーム動かしたとき、他のプロパティのキーは動かない。保存・復元後に値を照合する。

## 例外と復旧

同じプロパティの既存キーに重なる移動は競合位置を知らせ、元の位置へ戻せるようにする。他のプロパティの同時刻キーは独立に扱う。

## 参照資料と確認項目

- [A432](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/about-keyframes.html)　時刻の異なる二キーに透明度0と100を与え、中間時刻の描画が選んだ補間に従うか見る。（公開手順）
- [A433](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/add-keyframes.html)　現在位置にキーを追加して別時刻の値を変更し、追加されたキーの個数と時刻を照合する。（公開手順）
- [A434](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/select-keyframes.html)　矩形で複数キーを囲み、そのうち一点を選択解除して移動対象を確認する。（公開手順）
- [A435](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/copy-and-paste-keyframes.html)　三キーのまとまりを別位置へ貼り、各キー間のフレーム差と値が保たれるか見る。（公開手順）
- [A436](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/set-keyframes-to-snap.html)　スナップを切り替え、キーを既存の再生ヘッド近くまでドラッグして確定時刻を比べる。（公開手順）
- [A437](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/delete-keyframes.html)　三つのうち中央のキーだけを削除し、両端を結ぶ新しい途中値を確認する。（公開手順）
- [A440](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/view-keyframes-and-properties-in-the-timeline-panel.html)　タイムラインの表示プロパティを不透明度から音量へ切り替え、それぞれのキーの対象を区別する。（公開手順）
- [A441](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/view-keyframes-in-the-effect-controls-panel.html)　Effect Controlsでキーの時間軸を展開し、二つのプロパティのキーが同じ時刻で並ぶか照合する。（公開手順）
- [A442](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/move-current-time-indicator-to-keyframe.html)　前・次キーへの移動を繰り返し、再生ヘッドが選択プロパティの各キーの時刻に止まるか確認する。（公開手順）
