# MN-08 外部音声編集への送出 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

一つの音声とシーケンス全体を異なる単位で渡し、戻り先を記録する。

## 受入条件

一つの音声付き配置だけを渡す場合と全シーケンスを渡す場合で、生成した素材と戻り先の数・時刻を照合できる。

## 例外と復旧

選択に音声がないときは単体送出を無効にする。外部編集が中断しても元の音声を保持する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/edit-premiere-audio-clips-in-audition.html)
