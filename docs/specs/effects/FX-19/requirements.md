# FX-19 信号・リーダーの生成 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

黒、透過、色面、基準色と音、カウント用の素材を任意の尺で生成する。

## 受入条件

透明と黒を区別し、バーと基準音を映像・音声の経路確認に使える。

## 例外と復旧

対象出力にアルファや基準音のチャンネルが無い場合は該当経路を表示する。無効なレートや負の尺では素材を作成しない。

## 参照資料と確認項目

- [A461](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/create-a-counting-leader.html)　カウントリーダーを番組前に置き、開始と最後の基準フレームをタイムコードで確認する。（公開手順）
- [A462](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/calibrate-audio-and-video-using-bars-and-tone.html)　カラーバーと基準音を生成し、映像スコープの帯と音声の1 kHz成分を測る。（公開手順）
- [A463](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/create-black-video-clips.html)　下に明るい画像を置いて黒ビデオを重ね、黒マットと透明の違いを確認する。（公開手順）
- [A464](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/create-color-matte-clips.html)　指定RGBのカラーマットを作り、配置の長さを伸ばしても同じ色が表示されるか確かめる。（公開手順）
- [A465](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/create-transparent-video-clips.html)　透明ビデオを上段に置き、何も加えない時には下層の画が通ることを確認する。（公開手順）
