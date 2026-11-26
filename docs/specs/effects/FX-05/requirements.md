# FX-05 効果プリセット — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

効果群とキーを保存し、再適用時に開始端、終了端または尺を基準に配置する。

## 受入条件

長さの違う二つのクリップに同じプリセットを適用し、キー位置を確認する。

## 例外と復旧

短い適用先でキーが区間外になる場合は該当キーを表示し、適用中止を選べる。取消で適用先の既存キーを保持する。

## 参照資料と確認項目

- [A398](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/effect-presets.html)　始点基準・終点基準・尺比例でキーを持つプリセットを長さの異なる二配置で見比べる。（公開手順）
- [A399](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/create-effect-presets.html)　処理順に意味のある二効果をプリセットへ保存し、再適用後も順序が等しいか確認する。（公開手順）
- [A400](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/apply-effect-presets.html)　保存した動きのプリセットを短いクリップに置き、最初と最後のキーの時刻を照合する。（公開手順）
