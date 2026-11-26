# FX-07 補間曲線 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

時間の値補間と画面上の移動経路の補間を個別に設定する。

## 受入条件

同じ両端値でも保持・線形・曲線の中間フレームが異なる。

## 例外と復旧

離散値に連続補間を指定した場合は使用可能な方式を表示する。時刻が逆転する時間ハンドルは確定前に制限する。

## 参照資料と確認項目

- [A438](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/keyframes-and-graphs-in-panels.html)　同一プロパティを時間軸とグラフで表示し、キーの時刻と値の対応を追う。（公開手順）
- [A439](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/edit-keyframes-graphs.html)　速度グラフのハンドルを動かし、開始値と終了値を維持したまま途中の加速度が変わるか試す。（公開手順）
- [A443](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/control-effect-changes-using-keyframe-interpolation.html)　同一の位置キーで時間補間だけを変え、軌道と到達速度のうち何が変わったか確認する。（公開手順）
- [A444](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/change-keyframe-interpolation-method.html)　中央キーを保持補間へ変更し、次キー直前の値と切替フレームを調べる。（公開手順）
- [A445](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/filter-properties-in-the-effect-controls-panel.html)　変更済み・キーフレーム付き項目で絞り込み、未変更の項目が編集内容ごと消えていないか見る。（公開手順）
- [A446](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/adjust-or-reset-controls-in-the-effect-controls-panel.html)　回転だけをリセットし、同じMotion内の位置と別の効果の値が維持されるか照合する。（公開手順）
- [A447](https://helpx.adobe.com/premiere/desktop/add-video-effects/control-effects-and-transitions-using-keyframes/control-effect-changes-using-bezier-keyframe-interpolation.html)　ベジェの片側のハンドルを動かし、次区間の速度変化と隣接区間への影響を見る。（公開手順）
