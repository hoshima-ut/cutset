# AU-14 ラウドネス測定 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

瞬間ピーク、統合ラウドネス、トゥルーピークを別々に測定し、目標に合わせる。

## 受入条件

ピークが等しく平均の異なる素材で差を示す。全編を再生してLUFSとdBTPを記録し、納品先別の値は案件設定に持つ。

## 例外と復旧

無音だけの信号を有限の統合値として補正しない。必要なゲインがピーク上限を超える場合は両条件を示し、処理方針を選ばせる。

## 参照資料と確認項目

- [A535](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/auto-match-audio-loudness.html)　ピークが近く平均音量が異なる二台詞を自動一致させ、処理前後の統合ラウドネスを比較する。（公開手順）
- [A536](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/monitor-volume-levels.html)　瞬間的に過大な音を含む素材を流し、メーターのピーク表示と持続音の表示を見分ける。（公開手順）
- [A544](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/about-loudness-meter.html)　音量差の大きい素材を通し、トゥルーピークと統合ラウドネスが異なる指標として変化するか観察する。（公開手順）
- [A545](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/apply-loudness-meter-to-a-track.html)　ミックストラックへラウドネスメーターを挿し、複数の音源を足した最終信号を測れるか試す。（公開手順）
- [A546](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/measure-the-loudness-of-your-track.html)　測定値をリセットして番組全体を頭から再生し、短い部分再生と全編の測定値を区別する。（公開手順）
- [A547](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/edit-loudness-meter-settings.html)　測定単位と目標値を切り替え、メーターの目盛・警告表示と実際の音量を別々に確かめる。（公開手順）
