# 速度・逆再生の要件（ED-33）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

再生率、尺、ピッチ維持と後続移動を指定する。

## 受入条件

48フレームを倍速で24フレームにし、逆再生でフレーム番号が逆順になる。

## 例外と復旧

0や非数の速度指定を拒否する。素材不足またはロックされた後続がある場合は確定前に知らせる。

## 参照資料と確認項目

- [A244](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/different-ways-to-change-clip-speed-and-duration.html)　同じ素材に固定速度・尺指定・速度曲線を個別に適用し、開始と終了の間の素材時刻の進み方を比較する。（速度・尺は既存。複数音声ストレッチモード・高品質・新ピッチUIは27.0）
- [A245](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-using-the-speedduration-option.html)　速度とデュレーションの設定で倍速・逆再生・ピッチ維持を組み合わせ、尺と既知の音程を照合する。（速度・尺は既存。複数音声ストレッチモード・高品質・新ピッチUIは27.0）
- [A246](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-and-duration-using-the-rate-stretch-tool.html)　Rate Stretchでクリップを空き区間に合わせ、素材の最初と最後を使ったまま指定の尺に収まるか試す。（公開手順）
- [A250](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/freeze-a-video-frame-for-the-duration-of-a-clip.html)　選んだソースフレームでクリップ全尺を静止させ、冒頭・中央・末尾のフレーム番号がすべて同じか見る。（公開手順）

<a id="premiere-27-18"></a>

## 音声の時間伸縮方式と音程を選ぶ（27.0との照合）

再生速度、伸縮方式、音程を別々に保存する。[Adobeの公開資料](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-using-the-speedduration-option.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-18)と[受入試験](tasks.md#premiere-27-18)に記載する。
