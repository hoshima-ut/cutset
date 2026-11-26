# ダッキングの要件（AU-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

台詞などの基準信号に合わせて他の音を下げ、編集可能なカーブを作る。

## 受入条件

最後の歓声だけは手で残す。台詞編集後に再生成した際の手修正部分の扱いを記録する。

## 例外と復旧

入力トラックが削除された場合は生成済みカーブを保持する。音楽を会話側にも指定して自己検出する設定は受け付けない。

## 参照資料と確認項目

- [A531](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/automatically-duck-audio.html)　台詞と重なった区間だけBGMを下げるキーを生成し、台詞の前後に元の音量へ戻るか聴く。（既存ダッキングと、編集変更後にキーを自動再生成する27.0拡張を区別）

<a id="premiere-27-8"></a>

## 編集に追従する自動ダッキング（27.0との照合）

基準音声の追加、端のトリム、ミュートで該当時間と復帰区間の自動キーを更新する。[Adobeの公開資料](https://helpx.adobe.com/jp/premiere/desktop/add-audio-effects/adjust-volume-and-levels/automatically-duck-audio.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-8)と[受入試験](tasks.md#premiere-27-8)に記載する。
