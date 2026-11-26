# MN-05 交換データの出力 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

受け渡し目的と対象に合わせてタイムライン交換形式・対象範囲を選ぶ。

## 受入条件

素材選択時には有効な受け渡し方法だけを示し、シーケンスを対象にするとトラックを持つ形式を選べる。選んだシーケンスIDが出力に含まれる。

## 例外と復旧

複数の異なる種類を選択していたら対象選択へ戻す。未選択のアクティブシーケンスを代わりに出力しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-project-as-a-final-cut-pro-xml-file.html)
