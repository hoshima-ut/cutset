# 切替と素材余白の要件（ED-40）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

配置の端または隣接境界に遷移を置き、利用可能な余白で長さを制限する。

## 受入条件

余白あり・なしを含む3カットで、選択した箇所・種別だけが変わるか比較する。

## 例外と復旧

余白が足りない場合は短縮・片寄せ・取消を提示する。静止フレームの補間を無断で足さない。

## 参照資料と確認項目

- [A479](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/clip-handles-settings.html)　両側に余り素材のある境界と使い切った境界で同尺の切替を作り、反復フレームの有無を確認する。（26.0で映像トランジションの直操作、26.5で音・映像ハンドルの表示切替追加）
- [A480](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/video-transitions-using-clip-handles.html)　タイムラインの端ハンドルをドラッグして映像フェードを作り、伸縮時の長さとプレビューを確認する。（26.0で映像トランジションの直操作、26.5で音・映像ハンドルの表示切替追加）

<a id="premiere-27-15"></a>

## トランジションに足りないフレームを生成する（27.0との照合）

遷移の左右で必要な余白と実在フレームを数え、不足分だけを生成候補として示す。[Adobeの公開資料](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-overview.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-15)と[受入試験](tasks.md#premiere-27-15)に記載する。
