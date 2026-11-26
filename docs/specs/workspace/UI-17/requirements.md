# UI-17 欠落素材と音の診断 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

オフラインの配置を保持し、無音・欠落箇所から原因となる経路を辿れる。

## 受入条件

素材が消えても配置、素材ID、尺、字幕を保持。無音時は音源→トラック→ミキサー→機器で信号を追える。プラグイン不調、デコード失敗、壊れたキャッシュを区別し、復旧版に元案件を上書きしない。

## 例外と復旧

似たファイルを指定した場合は尺・メディア情報の差を示し、自動で全配置を別素材へ切り替えない。

## 参照資料と確認項目

- [A775](https://helpx.adobe.com/premiere/desktop/troubleshooting/audio-issues/search-for-clips-without-sound.html)　無音と判定したクリップを一覧化し、音声なしの素材とミュートした配置を区別する。（障害診断）
- [A776](https://helpx.adobe.com/premiere/desktop/troubleshooting/audio-issues/playback-issues-due-to-missing-sound-from-all-clips.html)　全トラック無音なら出力先とマスターの信号を比較し、復帰後のレベルを確認する。（障害診断）
- [A777](https://helpx.adobe.com/premiere/desktop/troubleshooting/audio-issues/playback-issues-due-to-missing-sound-from-some-of-the-clips.html)　一部素材だけ無音ならチャンネル割当と配置のミュートを対照クリップと比較する。（障害診断）
