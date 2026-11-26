# FX-15 自動画角調整 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

異なる縦横比に変換する際に被写体を追従し、結果を手で補正する。

## 受入条件

横動画を縦にし、二人が交差する場面を手直しする。元の横版・字幕位置も照合する。

## 例外と復旧

対象を見失った区間を示して固定中心または手指定を選べる。再解析時に手で固定したキーを保護する。

## 参照資料と確認項目

- [A450](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/auto-reframe-overview.html)　横長素材中で走者が左右を移動する場面を自動リフレームし、新画角内の被写体位置を追う。（既存機能。Windows RTXの追加高速化は27.0）
- [A451](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/add-auto-reframe-effect-to-a-sequence.html)　シーケンス全体から縦長版を作り、元シーケンスの寸法・クリップ位置が保たれているか確かめる。（26.2で自動リフレーム後のシーケンス解像度指定を拡張）
- [A452](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/add-auto-reframe-effect-to-a-clip.html)　二配置の片方だけにAuto Reframeを掛け、自動の座標を直した結果と未処理の配置を比べる。（既存機能。Windows RTXの追加高速化は27.0）
