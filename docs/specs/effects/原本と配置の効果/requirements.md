# 原本と配置の効果の要件（FX-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

原本を使う全配置への変更と、一つの配置への変更を区別する。

## 受入条件

同じ素材の二配置で、共通の補正と一配置だけの効果が保たれる。

## 例外と復旧

削除済み素材への操作は適用を止める。素材オフライン時は設定を保持し、再接続後に該当配置のキャッシュを無効化する。

## 参照資料と確認項目

- [A405](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/about-source-clips.html)　同一素材を二箇所へ配置し、Project項目と各配置の選択で見える効果の作用範囲を比較する。（公開手順）
- [A406](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/apply-effects-to-source-clips.html)　Source側で白黒効果を足し、異なるシーケンスで使っている同じ素材がともに白黒になるかを見る。（公開手順）
- [A407](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/enable-or-disable-source-clips-effects-in-thumbnails.html)　Source効果のサムネール表示を切り替え、素材一覧の絵とタイムライン出力を別々に照合する。（公開手順）
