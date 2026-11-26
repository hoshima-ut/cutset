# IO-32 プレビューの計算 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

選択範囲のプレビューを生成・破棄し、編集後は影響範囲だけ無効にする。

## 受入条件

エフェクトの変更前後で古い絵が残らず、レンダーし直してもカット点と尺が一致することを確認。

## 例外と復旧

旧版の計算が編集後に完了しても現行プレビューに採用しない。失敗した範囲は原本再生へ戻せる。

## 参照資料と確認項目

- [A627](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/render-a-section-of-a-sequence.html)　赤い区間の一部をIn/Out指定してレンダーし、対象区間のプレビュー表示と再生状態がどう変わるか確認する。（公開手順）
- [A630](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/use-preview-files-when-rendering.html)　低解像度のプレビュー利用をオン・オフして2本を書き出し、再利用と処理時間・画質の関係を比べる。（公開手順）
- [A631](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/delete-preview-files.html)　選択範囲のプレビューを消して元素材と編集を保持し、その範囲を再レンダーできるか試す。（公開手順）
- [A784](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/troubleshoot-sequence-and-file-interpretation-settings.html)　解釈したfpsとシーケンスfpsを比較し、意図したプルダウンと誤設定を区別する。（障害診断）
