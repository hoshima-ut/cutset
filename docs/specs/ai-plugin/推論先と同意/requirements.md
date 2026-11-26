# 推論先と同意の要件（AI-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

案件単位に推論先を選択し、各要求で外部に出る媒体と範囲を確認できる。

## 受入条件

素材送信を許さない案件では外部へ送らず、手編集や採用済みの結果をオフラインで再生できる。

## 例外と復旧

認証失効、上限超過、組織の送信禁止を区別する。有料APIや別接続先へ自動切替せず、キャンセル後も手編集を継続できる。

## 参照資料と確認項目

- [A024](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/ai-models-preferences.html)　モデルの準備状態を表示し、未取得モデルを必要とする操作だけに理由を出す。（公開手順）
- [A315](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/about-cloud-based-ai-voice-features.html)　クラウド音声AIの機能ごとに提供開始版を照合し、対象版で外部に送る音声範囲を実行前に説明できるか調べる。（クラウド音声サービス条件。Separate Crosstalkの正式機能は27.0）
- [A738](https://helpx.adobe.com/premiere/desktop/premiere-ai-assistant/assistant-faq.html)　27系の比較環境で接続・対象条件を変え、FAQ記載の利用条件と実際に表示される制限を照合する。（27.0正式のAI Assistant。26系正式の対象外）
