# 役割別の音作りの要件（AU-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

会話、音楽、効果音、環境音の分類を修正し、対象ごとに処理を選ぶ。

## 受入条件

音楽を台詞へ再指定したときに使える操作、単クリップと複数選択の適用範囲を確認する。

## 例外と復旧

手動調整を含む処理が役割変更で無効になる場合は確認を求める。混在値を表示しただけで各配置の値を揃えない。

## 参照資料と確認項目

- [A525](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/audio-category-tagging.html)　台詞、音楽、効果音、環境音を自動分類し、誤分類を手で直した後のタグを再読込する。（公開手順）
- [A527](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/audio-editing-with-essential-sound-panel.html)　四種類の音声へ役割を指定し、同じパネルで役割ごとに使える調整を切り替えて試聴する。（公開手順）
- [A532](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/create-audio-presets.html)　独自の台詞処理を音声プリセットとして保存し、別クリップに呼び出して設定値を照合する。（公開手順）
