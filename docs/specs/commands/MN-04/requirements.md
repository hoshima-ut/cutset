# MN-04 案件の一部を読み込む — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

取り込み対象が案件なら必要なシーケンスとビンを選択する。

## 受入条件

別案件の二シーケンスから一つだけ取り込む。コピーの編集後に元案件を開くと、そちらの配置と尺は維持されている。

## 例外と復旧

読み込み中に元案件の版が変わったら使用版を表示し、失敗時は部分的なビンや配置を残さない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-projects-as-project-shortcuts.html)
