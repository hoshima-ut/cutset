# 画面上の文字組みの要件（GR-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

ポイント文字、段落枠、書体、字間、塗り、縁取りを調整する。

## 受入条件

日本語・英数混在、長い氏名、改行、フォント欠落で文字のあふれと行高を確認する。

## 例外と復旧

書体未導入や未収録字形を区別し、代替書体と対象箇所を示す。代替表示で保存しても指定書体名を維持する。

## 参照資料と確認項目

- [A333](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/create-titles.html)　画面上のクリックで短い見出し、ドラッグで長文枠を作り、折り返しの違いを観察する。（公開手順）
- [A342](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/use-color-fonts.html)　色付き字形を含むフォントでタイトルを作り、プレビューと書き出した静止画の色を照合する。（公開手順）
- [A343](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/use-emojis.html)　絵文字を文字列の途中に配置し、保存・再開後に字形とベースラインが一致するかを見る。（公開手順）
- [A355](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/mask-with-text-or-shape-using-properties-panel.html)　文字の形をマスクに使い、文字の内側にだけ動画が現れることを透過部分で確かめる。（公開手順）
- [A360](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/edit-text-in-graphics-tab.html)　Graphicsタブから離れた二つのテロップを順に直し、各変更が該当する時間にだけ出るか見る。（公開手順）
