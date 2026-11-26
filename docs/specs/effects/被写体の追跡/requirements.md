# 被写体の追跡の要件（FX-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

指定被写体を時間方向に追跡し、誤ったフレームを手で修正して継続する。

## 受入条件

横切る人物・髪・同系色背景で試し、キャッシュを持たない端末への移動後は再構築結果も確認する。

## 例外と復旧

遮蔽や信頼度低下で未確定のフレームを示す。中断後は手修正済みのアンカーを残し、未解析区間から再開できる。

## 参照資料と確認項目

- [A482](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/object-masking.html)　移動する人物をクリックしてObject Maskを作り、背景の似た別人を選ばないか確認する。（26.0でObject Mask。26.3で追跡・復元改善、27.0のファイル管理・追跡改善は別）
- [A488](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/mask-tracking-tools.html)　移動だけの被写体と拡大回転する被写体を用意し、追跡の選択肢ごとの輪郭のズレを調べる。（公開手順）
- [A489](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/adjust-masks-at-the-clip-or-frame-level.html)　1フレームだけの修正とクリップ全体への修正を試し、前後フレームのマスク位置を比較する。（公開手順）
- [A490](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/track-masks.html)　ショット中央から前方・後方に追跡し、遮蔽地点で補正後に手前の正しい区間が維持されるか試す。（公開手順）
- [A492](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/apply-sharp-and-smooth-modes-in-object-masking.html)　髪と硬い物体の境界でSharpとSmoothを切り替え、同一フレームのアルファを比べる。（26.2でSharp／Smooth選択、26.5で滑らかさ調整を拡張）

## オブジェクトマスクの境界と追跡

開始フレームの被写体を選び、シャープまたはスムーズを選択して前後に追跡する。硬い小道具では境界の内外を分け、髪の毛や動きぼけでは中間の透明度を残す。遮蔽から被写体が戻ったフレームを指定して追跡を再開できる。

[Premiere 26.x との照合](../../premiere-releases-2026-11.md)

<a id="premiere-27-14"></a>

## 追跡マスクの保存と復元（27.0との照合）

手修正アンカーを案件に保持し、追跡結果には元素材との対応と版を記録する。[Adobeの公開資料](https://helpx.adobe.com/jp/premiere/desktop/add-video-effects/work-with-masks/mask-tracking-tools.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-14)と[受入試験](tasks.md#premiere-27-14)に記載する。
