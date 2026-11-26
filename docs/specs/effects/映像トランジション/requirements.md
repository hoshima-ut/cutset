# 映像トランジションの要件（FX-16）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

位置、長さ、揃え方、曲線を指定して片側または両側に遷移を置く。

## 受入条件

十分な余りフレーム、片側不足、両側不足を比較し、反復する端フレームと隣の実素材の違いを表示で確認する。

## 例外と復旧

余長不足時は不足する側とフレーム数を表示し、尺短縮・揃え方変更・反復の採否を選択する。

## 参照資料と確認項目

- [A408](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-video-transitions.html)　ワイプとディゾルブを同じ編集点に順に置き、AからBへの境界形状を一時停止して比較する。（版混在。3D Spinback／Slideは26.2、Shape Dissolveは26.3）
- [A409](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-video-dissolve-transitions.html)　指定色へのディップとクロスディゾルブを適用し、中央フレームの色の違いを調べる。（既存ディゾルブ群。Shape Dissolveの追加は26.3）
- [A426](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/transition-effects.html)　濃淡マップを反転してGradient Wipeを再生し、どちら側が先に現れるか照合する。（公開手順）
- [A466](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/transitions-overview.html)　クリップ間・端・VRの各対象を用意し、トランジションを置ける境界と描画を比較する。（公開手順）
- [A467](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/set-and-apply-default-transitions.html)　既定の切替を変更して二つの編集点へ既定操作を行い、指定した効果名が追加されるか見る。（公開手順）
- [A468](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/apply-single-sided-transitions.html)　間に空白を置いたクリップの終端だけへ切替を置き、次のクリップに切替が付かないか確認する。（公開手順）
- [A469](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/copy-and-paste-transitions.html)　尺を変えたディゾルブを別編集点に貼り付け、種類・尺と余り素材不足時の見え方を比較する。（公開手順）
- [A470](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/align-transitions.html)　開始揃え・中央揃え・終了揃えを切り替え、編集点と切替の両端のフレーム差を測る。（公開手順）
- [A471](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/reposition-the-center-of-a-transition.html)　切替の中央位置を前にずらし、両素材が見えるフレームと元のカット点との関係を確認する。（公開手順）
- [A472](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/change-transition-settings.html)　同じワイプの方向を変更し、中央フレームで新しい映像が現れる側が変わるかを見る。（公開手順）
- [A473](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/replace-transitions.html)　長さを指定した切替を別の種類へ置換し、編集点・尺・両側の素材の開始位置を再点検する。（公開手順）
- [A474](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/move-cuts-and-transitions-simultaneously.html)　切替が付いた編集点をまとめて移動し、隣のカットと切替の相対位置をフレームで照合する。（公開手順）
- [A475](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/change-transition-duration-using-the-effect-controls-panel.html)　Effect Controlsでトランジションを12フレームに設定し、タイムライン上の両端で長さを確認する。（公開手順）
