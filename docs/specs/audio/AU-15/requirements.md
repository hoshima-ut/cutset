# AU-15 タイムラインでの収録 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

入力機器・宛先・開始点を指定し、カウント後に録音したテイクを配置する。

## 受入条件

入力未選択、録り直し、開始終了位置、テイクの原本を確認する。

## 例外と復旧

機器切断や容量不足時は収録を停止し、取得できた範囲と回復可能なテイクを明示する。空ファイルを完成テイクとして登録しない。

## 参照資料と確認項目

- [A121](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/record-audio.html)　入力機器と録音先を指定して短いテイクを録音し、新しい音声ファイルの長さと実際の音を確認する。（既存録音機能。Voice-Over／ミキサー録音中に波形をリアルタイム描画する拡張は27.0）
- [A122](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/record-a-voice-over-on-an-audio-track-from-the-timeline.html)　録音したいトラックのマイクボタンでナレーションを入れ、開始位置と配置先が選んだトラックに一致するか聴く。（既存録音機能。Voice-Over／ミキサー録音中に波形をリアルタイム描画する拡張は27.0）
- [A123](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/record-audio-using-the-audio-track-mixer.html)　ミキサーで録音対象トラックを準備し、二つの入力から指定したチャンネルだけが記録されたか照合する。（既存録音機能。Voice-Over／ミキサー録音中に波形をリアルタイム描画する拡張は27.0）
- [A124](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/mute-input-during-recording.html)　マイク入力を録音中だけモニターミュートし、返しの音が消えても録音ファイルに発声が残るか聴く。（公開手順）
