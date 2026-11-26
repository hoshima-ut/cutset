# 球面効果の要件（FX-21）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

球面上の方向・継ぎ目・左右眼の関係を保って回転・フィルター・切替を適用する。

## 受入条件

左右・天頂・経度の継ぎ目で映像を確認し、首振りに応じた音の向きを試聴する。

## 例外と復旧

投影や音場のチャンネル順が不明な素材では明示指定を求める。通常のステレオ音声に球面回転を一律適用しない。

## 参照資料と確認項目

- [A298](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/immerse-video-effects-and-transitions.html)　球面対応の効果・トランジションを境界線をまたぐ被写体に適用し、全天球ビューで縫い目を点検する。（公開手順）
- [A299](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/three-axis-video-rotation.html)　既知の正面・天頂・水平線を持つ映像を3軸ごとに回し、意図した方向だけが変わったか測る。（公開手順）
- [A417](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/immersive-video-effects.html)　球面素材にVRぼかしを掛け、正面と背面のつなぎ目をまたいで再生する。（公開手順）
