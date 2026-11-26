# 基本補正の要件（CO-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

白点、露光、コントラスト、明暗域、彩度を個別または自動で調整する。

## 受入条件

自動設定後に各値を編集できる。色票の中立色と肌、露出の飽和箇所を確認する。

## 例外と復旧

飽和パッチや完全な黒が白点の試料の場合は採取をやり直せる。未確定の自動値で処理済みの手動設定を上書きしない。

## 参照資料と確認項目

- [A460](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/create-vignettes-using-lumetri-color.html)　ビネットの量と丸みを順に変え、画面中央の顔と四隅の輝度変化をスコープで比較する。（公開手順）
- [A572](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/about-color-grading.html)　グレーチャートを基準に補正前後の黒・中間・白の変化をスコープで読む。（公開手順）
- [A573](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/basic-color-correction-options.html)　露光量・白・黒・彩度を順に一項目ずつ動かし、初期値への復帰を確認する。（公開手順）
- [A576](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/color-correction-workflow.html)　素材の解釈から納品まで同じチャートを通し、どの段で色が変わるか追う。（公開手順）
- [A577](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/about-color-correction-effects.html)　素材全体と配置クリップへの色効果の適用範囲を同じ素材の二配置で見分ける。（公開手順）
- [A578](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/available-color-correction-effects.html)　色補正効果を名前で選び、現在使える効果と旧案件用の効果を識別する。（公開手順）
- [A584](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/use-auto-color.html)　自動補正の結果を適用前と並べ、採用後も各調整値を手で直せるか確かめる。（公開手順）
