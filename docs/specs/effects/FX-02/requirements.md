# FX-02 配置の効果スタック — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

効果を重ね、順序・設定・有効状態を変更し、選択属性を別配置に転用する。

## 受入条件

「変形してから切り抜く」と逆順の差、一項目のリセット、隣接クリップへの影響を確認する。

## 例外と復旧

貼付先がロック済み、または値型が合わない場合は対象と理由を示し、確定前のスタックを保持する。

## 参照資料と確認項目

- [A391](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/apply-effects.html)　効果を一つの配置にドラッグし、同じ素材の二番目の配置まで変わっていないか確かめる。（公開手順）
- [A392](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/remove-effects-from-a-clip.html)　積んだ二つの効果の一方だけを取り除き、残る効果の値と順序を照合する。（公開手順）
- [A393](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/copy-and-paste-clip-effects.html)　キー付き効果を別クリップへ貼り付け、単一属性と複数属性の選択結果を比較する。（公開手順）
- [A395](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/about-effect-controls-panel.html)　タイムラインで隣の配置を選び、Effect Controlsの時間軸とプロパティが正しい対象へ切り替わるか見る。（既存パネル。音声・映像効果とマスクをPropertiesにカード表示するUIは27.0）
- [A396](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/adjust-controls-in-the-effect-controls-panel.html)　同じ数値をドラッグと直接入力で設定し、モニター上の位置と確定値を照合する。（公開手順）
- [A397](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/view-effects-in-the-effect-controls-panel.html)　効果の開閉を切り替え、既に適用した処理と時間変化する項目を見つけられるか確かめる。（公開手順）
- [A401](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/use-fx-badges.html)　固定プロパティを変更した状態と効果を追加した状態のFXバッジを見比べ、対応する設定を開く。（公開手順）
- [A729](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/edit-and-enhance-content.html)　ニュース素材の粗編集に映像補正と音声修正を加え、処理した箇所の前後を参照画と聞き比べる。（公開手順）
