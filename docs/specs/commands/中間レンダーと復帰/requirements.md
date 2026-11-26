# 中間レンダーと復帰の要件（MN-13）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

現在の選択が置換・復帰可能かを示し、適用前後の素材と尺を照合する。

## 受入条件

通常クリップと置換済みクリップを選び直してメニューを比較。復帰後に元の効果の値を変更できるか確認。

## 例外と復旧

中間素材が欠落していても元構成が読めれば復帰候補を示す。元構成が他の配置のものなら適用しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/render-and-replace-media-in-a-sequence.html)
