# AU-03 サンプル単位の編集 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

映像フレーム未満の音声区間を波形で選んで編集する。

## 受入条件

48 kHzクリックの始点を映像フレーム未満の幅で移し、映像の編集点を維持する。

## 例外と復旧

元音声区間外へトリムした場合は利用できるサンプル範囲を示す。リサンプル時は素材側と出力側のレートを区別する。

## 参照資料と確認項目

- [A509](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/view-audio-and-video-waveforms-in-the-source-monitor.html)　Source Monitorで映像と波形を同時に表示し、口が開く直前の波形先端へ移動する。（26.2でSourceの映像と音声波形の併記を追加）
- [A510](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/edit-audio-using-the-properties-panel.html)　音声付きクリップを選びPropertiesから音量を変更し、選択外の台詞とレベルを比較する。（既存パネル。音声・映像効果とマスクをPropertiesにカード表示するUIは27.0）
- [A511](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/edit-audio-clips-in-the-source-monitor.html)　Source Monitorの波形でイン・アウトを設定し、編集点が指定した音節に来るか配置後に聴く。（公開手順）
- [A537](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/dynamic-audio-waveforms.html)　ダイナミック波形を切り替えてゲインを変え、波形の表示倍率と実際の出力を別々に照合する。（26系の表示中波形更新と録音時のライブ波形（27.0）を区別）
- [A539](https://helpx.adobe.com/premiere/desktop/add-audio-effects/adjust-volume-and-levels/live-waveform-editing.html)　ライブ波形に対応する版でクリップのレベルをドラッグし、操作中の波形外形と試聴の変化を比べる。（26系の表示中波形更新と録音時のライブ波形（27.0）を区別）
