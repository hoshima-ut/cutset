# ナレーションの取り込みの要件（IO-13）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

指定入力と宛先トラックで収録し、生成された音声を案件とタイムラインに登録する。

## 受入条件

モノラル入力の指定トラックだけに新規録音クリップができるか確認。モニターのミュートと録音ファイル内の音量を別に確認。

## 例外と復旧

入力の抜線や書込失敗が起きたら録音を止め、その時点で回収可能なデータと未登録の状態を示す。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/record-a-voice-over-on-an-audio-track-from-the-timeline.html)
- [公開資料 2](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/record-audio.html)
