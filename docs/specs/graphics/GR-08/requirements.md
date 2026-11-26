# GR-08 テンプレート交換 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

許可されたメディア枠・データを差し替え、再利用可能な形式へ出力する。

## 受入条件

異なる縦横比の素材や異なる値を投入し、再読み込み時の表示、テンプレートの制約を記録する。

## 例外と復旧

必須データの欠落、型違い、同梱できない素材を項目別に知らせる。未解決の枠を暗黙に別ファイルへ割り当てない。

## 参照資料と確認項目

- [A329](https://helpx.adobe.com/premiere/desktop/add-text-images/use-motion-graphics-templates/use-data-driven-motion-graphics-templates.html)　表データにある得点だけを更新し、対象の数値表示とチーム名を同時に照合する。（公開手順）
- [A330](https://helpx.adobe.com/premiere/desktop/add-text-images/use-motion-graphics-templates/media-replacement-in-motion-graphics-templates.html)　交換用の枠に縦長画像を入れ、画角の調整後も文字レイヤーが維持されているか確認する。（公開手順）
- [A331](https://helpx.adobe.com/premiere/desktop/add-text-images/use-motion-graphics-templates/where-do-i-get-motion-graphics-templates.html)　手元のテンプレートと提供ライブラリの候補を一つずつ探し、各入手元から追加できるか試す。（公開手順）
- [A353](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/export-graphic-as-a-motion-graphics-template.html)　編集可能な文字を含むグラフィックを.mogrtへ書き出し、別の空プロジェクトで配置して書き換える。（公開手順）
- [A358](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/working-with-these-motion-graphics-templates-in-premiere.html)　テンプレートを追加して公開された項目を編集し、シーケンスを書き出してプレビューと比較する。（公開手順）
