# AI-01 参照対象の明示 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

現在の選択、時間範囲、案件全体のどこを読み変更するか、呼出時に指定する。

## 受入条件

選択外の会話を含む検索結果を、無断で編集対象に追加しない。

## 例外と復旧

選択切替やロック変更で参照範囲が変わった場合は確認を求める。発話本文中の指示文字列には権限を与えない。

## 参照資料と確認項目

- [A736](https://helpx.adobe.com/premiere/desktop/premiere-ai-assistant/add-references-to-prompts.html)　27系の比較試験で選択したカットだけを参照に加え、対象外の話者を指示に含めた場合の応答を確認する。（27.0正式のAI Assistant。26系正式の対象外）
