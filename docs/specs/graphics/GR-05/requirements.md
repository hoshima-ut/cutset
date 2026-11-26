# GR-05 再利用するスタイル — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

文字と字幕の共有スタイルを定義し、局所上書きとの関係を保持する。

## 受入条件

複数テロップを更新し、個別に変えた文字、別スタイルの字幕、素材本体に波及した範囲を確認する。

## 例外と復旧

共有スタイル削除前に利用箇所を示す。参照を解除する場合は、その時点の見た目をローカル値として維持できる。

## 参照資料と確認項目

- [A334](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/create-text-styles.html)　文字の塗りとサイズからスタイルを保存し、新しい文字レイヤーに同じ見た目を適用する。（公開手順）
- [A335](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/apply-style.html)　見出し内の選手名だけを選んでスタイルを当て、前後の文字の装飾が維持されるかを見る。（公開手順）
- [A336](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/style-parameters-when-applying-from-style-browser.html)　文字色と配置の異なる二つのタイトルに同じスタイルを適用し、共有される属性を記録する。（公開手順）
- [A337](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/create-linked-and-track-styles.html)　タイトル用リンクスタイルと字幕用トラックスタイルを作り、各対象から呼び出せるか確かめる。（公開手順）
- [A338](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/apply-linked-and-track-styles.html)　同じ字幕トラックの二項目にトラックスタイルを適用し、隣の言語トラックへの影響を調べる。（公開手順）
- [A339](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/redefine-linked-and-track-styles.html)　共有スタイルの縁取りを再定義し、連動するタイトルとリンクしていないタイトルを比較する。（公開手順）
- [A340](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/parameters-when-applying-as-linked-style-or-track-style.html)　個別配置した字幕にトラックスタイルを当て、字形・装飾・位置のどの項目が引き継がれるか確かめる。（公開手順）
- [A354](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/create-source-graphics.html)　既存グラフィックをSource Graphicに変えて複数配置し、共通内容の変更が各配置に現れるか見る。（公開手順）
- [A730](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/incorporate-branded-graphics-and-audio-elements.html)　共通の局ロゴ、テロップ、ジングルを配置し、別の編集端末でも同じ位置とレベルで再現できるか試す。（公開手順）
