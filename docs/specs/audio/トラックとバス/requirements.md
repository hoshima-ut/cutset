# トラックとバスの要件（AU-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

各トラックをバス・送信・出力へ配線し、レベル・パン・ソロ・ミュートを制御する。

## 受入条件

センドのプリ／ポストフェーダーと挿入効果の位置を変え、元フェーダー操作が各経路へどう届くかを試聴する。

## 例外と復旧

直接または複数バスを経由して自身へ戻る接続は拒否し、問題の経路を表示する。バス削除時は接続先の付替えを確認する。

## 参照資料と確認項目

- [A514](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/about-audio-track-mixer.html)　一つのトラックのソロ／ミュート／フェーダーを動かし、隣のトラックと最終出力を同時に観察する。（公開手順）
- [A515](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/create-a-submix.html)　台詞二トラックをサブミックスへ送り、そのフェーダーだけで両方の声が動き音楽が保たれるか聴く。（公開手順）
- [A534](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/adjust-track-volume.html)　トラックのフェーダーで後続クリップを含めてまとめて下げ、隣のトラックのメーターを比較する。（公開手順）
- [A551](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/audio-panning-and-balancing-controls-in-audio-track-mixer.html)　モノ音源のパンとステレオ音源のバランスを同じ位置にし、左右出力の変化の違いを観察する。（公開手順）
- [A552](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/pan-or-balance-a-stereo-track.html)　左右で異なる話者のステレオトラックを片側へ寄せ、各話者の出力レベルを個別に比較する。（公開手順）
- [A553](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/pan-or-balance-an-adaptive-track.html)　複数成分のアダプティブトラックで送り先を変え、対象の成分だけが目的の出力へ届くか確かめる。（公開手順）
- [A554](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/pan-or-balance-a-track-in-timeline.html)　タイムライン上のパンキーを左から右へ描き、通過する再生位置に従って定位が移るか聴く。（公開手順）
