# 字幕ファイルの出力の要件（MN-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

選択した字幕トラック・範囲・言語をファイルとして書き出す。

## 受入条件

字幕なしでは未実行の理由が読める。二言語の字幕がある案件では選んだ言語だけが指定先に出る。

## 例外と復旧

対象キューがない場合は理由を示し、意図しない空ファイルを保存しない。

## 参照資料と確認項目

- [公開資料 1](https://community.adobe.com/bug-reports-728/reporting-a-missing-keyboard-shortcut-bug-1331727)
