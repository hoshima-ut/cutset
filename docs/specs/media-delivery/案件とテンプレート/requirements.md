# 案件とテンプレートの要件（IO-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

保存先とひな型を指定して、空または所定のビン構成の案件を作る。

## 受入条件

空案件とテンプレート案件を別の保存先で作り、ひな型のビンとシーケンスの有無が意図どおりか確認。

## 例外と復旧

同名ファイルがある場合は保存先の再選択へ戻す。作成に失敗した案件は最近使った一覧に加えない。

## 参照資料と確認項目

- [A104](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/start-projects.html)　空の案件に素材とシーケンスを入れて保存し、再度開いたときに参照先と編集結果が復元されるか試す。（公開手順）
- [A105](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/create-new-project.html)　保存先と案件名を指定して新規作成し、後から同名の別フォルダーの案件と取り違えず開けるか試す。（公開手順）
- [A106](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/open-projects.html)　最近使った項目とファイル選択から同じ案件を開き、最終保存時のシーケンスが一致するか照合する。（公開手順）
- [A115](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/create-your-own-project-templates.html)　共通ビンとシーケンスを含むテンプレートから2案件を作り、片方の変更がひな型と他方に波及しないか確かめる。（公開手順）
