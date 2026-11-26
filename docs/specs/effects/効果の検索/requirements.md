# 効果の検索の要件（FX-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

対象の種類・処理精度・利用可能な実行経路で効果を探す。

## 受入条件

32-bit対応とGPU対応を独立して確認し、同名の旧版を識別できる。

## 例外と復旧

適用先の媒体や設備に合わない候補には理由を表示する。選択対象が変わったら効果追加前に可否を再評価する。

## 参照資料と確認項目

- [A383](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/about-effects-and-effects-panel.html)　Effectsでぼかしを探してクリップに置き、Effect Controlsで値を変えた結果をモニターで確認する。（既存Effectsパネル。サムネイル・動画プレビュー・自分の素材での効果試写は27.0）
- [A384](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/types-of-effects.html)　固定のMotionと追加した標準効果を選び、削除の可否と作用対象の違いを確かめる。（公開手順）
- [A385](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/list-of-accelerated-effects.html)　GPU照合対象の効果を選び、対応表示と対象端末での処理経路・表示結果を記録する。（公開手順）
- [A386](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/list-of-32-bit-effects.html)　32-bit対応表示を持つ効果を階調素材に適用し、高精度の中間値を含む箇所で比較する。（公開手順）
- [A387](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/list-of-yuv-effects.html)　YUV対応の印を持つ効果をYUV素材へ掛け、無処理区間との輝度・色差の変化を観察する。（公開手順）
- [A394](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/find-and-group-effects.html)　検索結果から頻用効果を独自のビンへまとめ、次回起動時に同じ候補が見つかるか試す。（既存Effectsパネル。サムネイル・動画プレビュー・自分の素材での効果試写は27.0）
- [A410](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/adjust-effects.html)　階段状グレーのLevelsを動かし、上限と下限に集まる階調を波形で確認する。（公開手順）
- [A411](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/blur-and-sharpen-effects.html)　細い線に方向ぼかしとシャープを個別適用し、輪郭の広がりとエッジの強さを比較する。（版混在。Channel Blurは26.2、現行資料のRadial Blur等の新版追加は27.0）
- [A412](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/channel-effects.html)　特定チャンネルだけを反転して、原色パッチで他のチャンネルの値を照合する。（公開手順）
- [A413](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/color-correction-effects.html)　Video Limiterを高輝度パッチに掛け、制限前後の波形上端を比べる。（公開手順）
- [A414](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/distort-effects.html)　Corner Pinで右上の角だけをずらし、残り三点の位置と内部の変形を確認する。（26.5でTwirlを再構築し従来版はLegacy）
- [A415](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/generate-effects.html)　四点グラデーションで左上の色だけを変更し、四隅と中央の変化を確認する。（26.2でGradient、26.5でLens Flareの新版を追加）
- [A416](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/image-control-effects.html)　選んだ赤だけを残す画像処理を行い、背景の低彩度部分との境界を見る。（公開手順）
- [A421](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/noise-and-grain-effects.html)　無地グレーにノイズを掛け、無彩色と色付きの設定でチャンネル間の粒の違いを見る。（26.2でFilm ImpactによるNoise効果を追加）
- [A422](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/perspective-effects.html)　透明背景の文字に影を追加し、距離・方向を変えて文字の不透明部分に対する位置を測る。（公開手順）
- [A423](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/stylize-effects.html)　細かな数字にモザイクとポスタリゼーションを別々に適用し、面の分割と色段数の違いを確認する。（26.5でMosaicのソフトネス調整を更新。現行効果一覧との名称差を実機照合）
- [A427](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/utility-effects.html)　Cineon素材の変換で黒白点を順に変え、モニターと書き出した階調を比較する。（公開手順）
- [A428](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/video-effects.html)　映像効果の参照項目を実機検索し、該当効果を一つの標準クリップへ加えた描画の差を記録する。（公開手順）
- [A458](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/add-lightning-effects.html)　対象ビルドで使用可能な稲妻効果を調べ、旧案件での描画と新規追加の可否を分けて記録する。（公開手順）
