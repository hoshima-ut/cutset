# 変形とアンカーの要件（FX-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

基準点、位置、回転、倍率を画面のハンドルと数値で同期させる。

## 受入条件

アンカー変更後の回転中心、縦横比ロック、ベクター文字を拡大した輪郭を確認する。

## 例外と復旧

幅または高さが未確定の素材で比率が計算できない場合は比率維持操作を保留し、元の変形値を表示する。

## 参照資料と確認項目

- [A425](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/transform-effects.html)　非対称な矢印を水平反転してからOffsetを動かし、画面反対側への回り込みを確認する。（公開手順）
- [A453](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/apply-motion-effect.html)　アンカーを左端に置いて回転し、設定した端点を中心に絵が動くか確認する。（公開手順）
- [A454](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/edit-vector-graphics-using-vector-motion-effect.html)　ベクター文字へVector Motionの拡大を掛け、同じ大きさのラスター画像と輪郭を比較する。（公開手順）
