# 音声の取り込みの要件（IO-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

サンプルレート・ビット深度・チャンネルを判定し、試聴用変換後も原本を参照する。

## 受入条件

44.1 kHzと48 kHzの音を48 kHzシーケンスに置き、末尾の合図音がずれず、キャッシュ再生成後も一致するか確認。

## 例外と復旧

非対応チャンネル配置はマッピングを促す。変換失敗時は原本を残し、未完成キャッシュを再生に使わない。

## 参照資料と確認項目

- [A129](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/importing-digital-audio.html)　サンプルレートとチャンネル数が異なる音声を読み込み、埋め込まれた左右テスト信号が正しい側から出るか聴く。（公開手順）
- [A130](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/audio-sample-rates-in-premiere.html)　44.1kHzの既知長の音声を48kHz案件で再生し、冒頭と末尾の同期、速度、音程を照合する。（公開手順）
- [A131](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/audio-conforming-specifications.html)　長尺圧縮音声の適合処理が終わった状態と再起動後を比較し、キャッシュ再生成時の同期ずれを記録する。（公開手順）
- [A499](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/extract-audio-from-clips.html)　映像付き素材から音声を抽出し、生成項目の長さ・チャンネルと元映像の音を照合する。（公開手順）
- [A787](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/imports-only-audio-in-project-bin.html)　音声のみで読み込まれたファイルの映像ストリーム・対応デコーダーを調べる。（障害診断）
