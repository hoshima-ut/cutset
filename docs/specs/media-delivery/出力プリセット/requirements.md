# 出力プリセットの要件（IO-41）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

再利用できる設定と簡易書き出しを提供し、適用後の実効値を確認する。

## 受入条件

同名の素材から別解像度を2本出力。プリセット再適用で個別に変更した色・音の設定がどうなるか表示する。

## 例外と復旧

端末に無いエンコーダーや適用不能な組合せは項目単位で表示する。既存ジョブへ新しいプリセットを遡及適用しない。

## 参照資料と確認項目

- [A133](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-and-export-presets.html)　プリセットをファイルに出して別環境で取り込み、名前と編集に使う設定値が一致するか確認する。（公開手順）
- [A656](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/quickly-export-a-video-file.html)　Quick Exportで保存先を変え、選択中シーケンスのみに指定プリセットが使われたか確認する。（公開手順）
- [A663](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/preset-manager-overview.html)　プリセットを提供元・ユーザー作成で絞り込み、同名でも目的の設定を選べるか確認する。（公開手順）
- [A664](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/create-and-save-custom-presets.html)　音声設定を変更したプリセットを新しい名前で保存し、別の案件で再適用して値を照合する。（公開手順）
- [A665](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/manage-presets.html)　ユーザープリセットを他端末へ移し、元のプリセットを削除しても既存成果物が残るか確かめる。（公開手順）
