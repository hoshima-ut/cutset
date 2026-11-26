# IO-55 音声ポスト受け渡し — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

AAF・OMFの経路ごとに有効な方向、チャンネル、ハンドルと音声の格納方式を示す。

## 受入条件

大きい案件を外部音声で出力。Pro Tools等でカット端を延ばし、ハンドル、トラック、開始時刻を照合。

## 例外と復旧

元音声の端や形式上限でハンドルを確保できなければ不足量を示す。検証していない受け手との互換性を成功として表示しない。

## 参照資料と確認項目

- [A136](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-avid-media-composer-project-files.html)　Avid由来の交換用ファイルを読み、クリップのソースタイムコード、トラック順、未解決の素材参照を照合する。（公開手順）
- [A654](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-omf-files-for-pro-tools.html)　音声クリップをハンドル付きOMFにしてPro Toolsで開き、切り返しの前に戻れる素材量を測る。（公開手順）
- [A655](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/supported-features-for-exporting-omf-files-for-pro-tools.html)　フェードと音量キーフレームを含むOMFを再生し、保持された項目と再設定が必要な項目を記録する。（公開手順）
- [A657](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-aaf-files.html)　大きな案件を外部音声方式のAAFで納品し、各クリップとチャンネルが受け手側で接続するか試す。（公開手順）
- [A666](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-from-avid-media-composer-to-premiere.html)　Avidで出力した交換ファイルをPremiereで開き、素材の再接続とシーケンスのカット数を比較する。（公開手順）
