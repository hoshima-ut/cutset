# キーとトラックマットの要件（FX-13）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

色または別レイヤーの明度・透明度からマットを生成し、縁と色かぶりを調整する。

## 受入条件

マット表示で半透明の髪を確認し、背景を白・黒に替えて縁を見る。隠したマットの意図しない映り込みも確認する。

## 例外と復旧

マットトラックがオフライン、または自分自身を参照する場合は範囲を示して修正を求める。解決前に既存設定を失わない。

## 参照資料と確認項目

- [A418](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/keying-effects.html)　同じ白黒マットを輝度キーとトラックマットで使い、透過領域と半透明部分を比較する。（公開手順）
- [A419](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/apply-and-customize-chromakey-using-the-ultra-key-effect.html)　緑背景をUltra Keyのスポイトで指定し、衣服の緑部分と髪の境界を背景色を替えて確認する。（公開手順）
- [A420](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/ultra-key-effect-parameters.html)　マット調整とスピル抑制を別々に変え、緑かぶりとアルファがどう変わるか照合する。（公開手順）
