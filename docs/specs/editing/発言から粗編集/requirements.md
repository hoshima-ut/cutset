# 発言から粗編集の要件（ED-44）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

離れた複数の発言を選び、素材への対応を保って新しい初稿に並べる。

## 受入条件

3箇所の採用発言から初稿を作り、各カットの前後を元の音から再調整できる。

## 例外と復旧

発言の一部が欠落・オフラインなら対象の行を示し、同じ発言文字を持つ別テイクへ自動置換しない。

## 参照資料と確認項目

- [A228](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/edit-sequences-using-text-based-editing.html)　文単位で発言を並べ替え、Timelineのカットと新しい読み順、元ファイルの発話位置が対応するか確認する。（公開手順）
- [A231](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/create-a-sequence-with-paper-edit.html)　離れた3発言をPaper Editで選び、選択件数・合計尺・プレビュー・新規シーケンスの実尺を照合する。（26.5でPaper Editによる複数発言のシーケンス化）
