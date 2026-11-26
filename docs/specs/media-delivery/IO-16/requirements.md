# IO-16 重複と条件検索 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

同一素材の参照をまとめ、条件検索の結果からビンと利用箇所に移動する。

## 受入条件

同階層と別階層の同名ビンを置き、統合後にすべての配置が正しい素材へ解決するか確認。

## 例外と復旧

ファイル名が同じでも内容や解釈が異なるものは候補に理由を表示し、自動統合から外す。

## 参照資料と確認項目

- [A143](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/search-options-in-premiere.html)　プロジェクト内の項目検索と素材内容検索に同じ語を入れ、検索対象と結果の違いを見分けられるか確かめる。（公開手順）
- [A144](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/find-assets-using-the-find-dialog.html)　Findでプロパティと条件を指定し、似た名称でも条件に合うテイクだけを選択できるか確認する。（公開手順）
- [A153](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/consolidate-duplicate-folders.html)　重複するビン階層を含む案件で統合を行い、残った階層と素材の所属、既存の配置数を確認する。（公開手順）
