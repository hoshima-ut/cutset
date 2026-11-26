# MN-32 素材一覧の表示切替 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

対象パネルの表示だけをリスト・カード等に切り替える。

## 受入条件

二つのビンを別のパネルで開き、片方の表示をリストに変える。もう片方の表示、順序、選択は変わらない。

## 例外と復旧

以前の選択が新しいフィルターで隠れた場合は非表示として扱い、別項目を選んだ状態で命令を発行しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customization-options-for-the-project-panel.html)
