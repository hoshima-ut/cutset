# フレーム送りとシャトルの要件（ED-05）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材・シーケンスのどちらでもフレーム送り、速度付き再生、範囲ループを行う。

## 受入条件

低解像度再生と実寸停止表示を往復しても編集点・書き出し寸法は変化しない。

## 例外と復旧

先頭で逆送り、末尾で正送りした場合は有効端に停止し、オーバーフローで反対端へ飛ばない。

## 参照資料と確認項目

- [A633](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/play-clips-in-source-monitor.html)　素材モニターで発言の前後を再生し、編集中シーケンスの再生ヘッドや内容に影響が出るか確認する。（公開手順）
- [A634](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/play-active-sequence-in-program-monitor.html)　シーケンスタブを切り替え、プログラムモニターの再生内容が現在のタブと一致するか見る。（公開手順）
- [A635](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/play-back-in-a-continuous-loop.html)　前後に目印のある短い区間をループさせ、境界で飛ばしたり重複したりするフレームを調べる。（公開手順）
- [A636](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/play-clips-with-preroll-and-postroll.html)　編集点の前後に識別音を置き、設定したプリロール・ポストロール内を試聴できるか確認する。（公開手順）
