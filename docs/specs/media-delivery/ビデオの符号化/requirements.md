# ビデオの符号化の要件（IO-42）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

寸法・時間軸・コーデック・プロファイル・ビットレートと中間形式を指定する。

## 受入条件

同じタイムラインをWeb配信・中間素材向けに書き出し、実ファイルの内部コーデック、解像度、データ率、fps、アルファを読み戻す。

## 例外と復旧

アルファ非対応や寸法制約に当たる場合は該当設定を示す。丸めやアルファ除去を黙って適用しない。

## 参照資料と確認項目

- [A653](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-options-in-premiere.html)　同じカットをファイル、交換データ、外部キューへ渡し、各経路でできる成果物を識別する。（公開手順）
- [A658](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/supported-export-file-formats.html)　候補の形式を映像・静止画・交換データに分け、OSごとの直接書き出しとキュー経由の選択可否を照合する。（公開手順）
- [A659](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/create-and-export-hdr-videos-for-youtube-on-mac.html)　MacでHDRの短尺動画を作り、検証用プレイヤーで色空間タグとハイライトの表示を確認する。（公開手順）
- [A660](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/overview-of-export-settings.html)　出力形式を切り替え、字幕埋め込みや多重化などの利用可能な項目が形式と整合するか調べる。（26.5でMatch Sourceが音声チャンネル・サンプルレートに対応）
- [A661](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/basic-video-settings.html)　縦長・非正方形ピクセルの素材でMatch Sourceと寸法の手動指定を比較し、円の形を確認する。（公開手順）
- [A662](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/video-encoding-settings.html)　同一のH.264素材を異なるビットレートで出力し、ファイル内部のプロファイルとデータ率を読み直す。（公開手順）
