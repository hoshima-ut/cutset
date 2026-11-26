# 手ぶれ補正の要件（FX-14）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

動きを解析し、安定化量と画面端の扱いを指定して処理前後を比較する。

## 受入条件

パンを残す設定と固定したい設定を比較し、外縁と拡大による解像感を確認する。

## 例外と復旧

追跡点の少ないフレームやシーンの切れ目で補正が飛ばないよう区間を分ける。不足時は補正を無効化して原画を再生できる。

## 参照資料と確認項目

- [A455](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/stabilize-shaky-footage-using-warp-stabilizer.html)　手持ち撮影の一部を解析し、解析後の水平線、発生したトリミング、元のパンを確認する。（公開手順）
- [A456](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/warp-stabilizer-settings.html)　手ぶれ補正の滑らかさとフレーミングを別々に変更し、画角と動きの変化量を記録する。（公開手順）
