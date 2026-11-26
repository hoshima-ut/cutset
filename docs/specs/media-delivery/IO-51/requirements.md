# IO-51 選択シーケンスの取り込み — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

別案件から必要なシーケンスと依存素材を選んで取り込む。

## 受入条件

別案件に同名の素材を用意し、選択したシーケンスと関連素材のみが入る条件、既存素材の再利用条件を照合。

## 例外と復旧

不足依存と循環参照を示し、解決しない取り込みを途中の項目だけ残して確定しない。

## 参照資料と確認項目

- [A132](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-projects-as-project-shortcuts.html)　他案件へのショートカットから元案件を開き、参照先の移動時に何を再指定する必要があるか確かめる。（公開手順）
- [A134](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-selected-premiere-sequences.html)　複数シーケンスを持つ外部案件から一つを選んで読み込み、必要な従属素材だけで開いて再生できるか確認する。（公開手順）
