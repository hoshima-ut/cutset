# GR-06 テロップとフォントの検索 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

タイトル本文や書体を見つけて置換し、未解決のフォントを示す。

## 受入条件

同じ氏名を含むテロップと字幕を用意し、変更対象を取り違えない。

## 例外と復旧

検索後にテキストが変わった行は再確認を求める。未導入書体を同名のスタイルや別素材名で置き換えない。

## 参照資料と確認項目

- [A341](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/replace-fonts.html)　一つの書体を代替書体に置換し、別書体の見出しと改行の位置を見比べる。（公開手順）
- [A356](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/find-and-replace-text-using-the-graphics-tab.html)　画面タイトルの旧チーム名を置き換え、同じ名前がある文字起こしと字幕も比較する。（公開手順）
- [A357](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/check-spelling-using-the-graphics-tab.html)　誤綴りと登録済み固有名詞を含む画面文字で、候補の採用と無視をそれぞれ試す。（公開手順）
- [A745](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/ui-errors-when-using-obsolete-effects-in-on-macos-dark-mode.html)　旧効果の設定をmacOSの明暗両テーマで開き、UIの描画異常と映像レンダーを別に見る。（障害診断）
