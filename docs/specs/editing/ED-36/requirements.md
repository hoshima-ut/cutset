# ED-36 素材の時間・画素解釈 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

原本のバイト列を保ち、読み取るレート、画素比、フィールド、アルファを変更する。

## 受入条件

非正方ピクセル素材の円が円に見え、同一素材の別配置の扱いも確認できる。

## 例外と復旧

非対応の画素比や分母0のレートは保存できない。検出値に戻す操作は元ファイルを書き換えない。

## 参照資料と確認項目

- [A211](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/aspect-ratios.html)　同じテスト図形で画面自体の縦横比と各ピクセルの縦横比を変え、二つの設定が映り方に及ぼす差を確認する。（公開手順）
- [A212](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/frame-aspect-ratio.html)　横1920×縦1080と縦1920×横1080を同じ素材で比較し、枠の向きとカット内容が別の設定であると確かめる。（公開手順）
- [A213](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/pixel-aspect-ratio.html)　非正方ピクセルの撮影素材を正しいピクセル比で表示し、基準円の幅と高さが一致するか測る。（公開手順）
- [A214](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/set-the-aspect-ratio-of-a-sequence.html)　縦型のシーケンス寸法を指定し、プレビューと書き出しファイルの縦横寸法が同じか照合する。（公開手順）
- [A215](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/aspect-ratio-preservation.html)　横素材を縦枠に収める際、全体表示時の余白と画面を満たす際の切れを比較し、人物が伸縮しないか見る。（公開手順）
- [A216](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/correct-aspect-ratio-misinterpretations.html)　メタデータのピクセル比が誤った素材で解釈を指定し直し、原ファイルを変えずに基準図形のゆがみが直るか確認する。（公開手順）
- [A276](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/change-the-frame-rate-of-a-clip.html)　元ファイルの解釈フレームレートを変え、同一フレーム数の再生尺がどれだけ変わるか確かめる。（公開手順）
- [A277](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/about-interlaced-video.html)　左右に動く模様の二つのフィールドを片方ずつ再生し、走査線の組み合わせと撮影時刻の順を確認する。（公開手順）
- [A278](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/change-the-field-order-of-a-clip.html)　誤ったフィールド順の素材で解釈を反転し、動体の往復ぶれが改善するか原本と比較する。（公開手順）
- [A279](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/create-interlaced-or-non-interlaced-clips.html)　同じインターレース信号からフィールド処理ありの映像を作り、動体の斜線と細線の見え方を比較する。（公開手順）
- [A280](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/modifying-clip-properties-with-interpret-footage.html)　Interpret Footageでアルファとピクセル比の解釈を変え、半透明エッジと基準円を別々に確認する。（公開手順）
- [A756](https://helpx.adobe.com/premiere/desktop/troubleshooting/media-issues/eliminate-flicker.html)　細線の素材でちらつき軽減を適用し、縞の残り方と輪郭の変化を比べる。（障害診断）
