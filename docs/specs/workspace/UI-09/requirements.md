# UI-09 時間と整列の表示 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

タイムコードの表記とスナップ・ルーラー・ガイドの単位を選べる。

## 受入条件

29.97ドロップフレームと整数fpsを区別し、表示形式を変えても同一の映像コマを指す。表示用ガイド、セーフマージン、オーバーレイは通常の納品ファイルに含めない。

## 例外と復旧

ドロップフレームで存在しないフレーム番号を手入力した場合は値を確定せず、有効な形式を示す。

## 参照資料と確認項目

- [A164](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/about-timecode.html)　素材タイムコード開始が01時の映像を0開始のシーケンスへ置き、同じ絵に二つの異なる時刻が対応するか確認する。（公開手順）
- [A165](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/enter-timecode.html)　時刻欄に絶対時刻と相対移動量を入力し、目的のフレーム番号と移動後の表示を照合する。（公開手順）
- [A166](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/view-sequence-timecode.html)　開始時刻を設定したシーケンスで再生ヘッドを動かし、時間軸とProgram側の現在時刻が一致するか確認する。（公開手順）
- [A167](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/choose-timecode-display-format.html)　29.97fps素材をドロップフレーム表記にし、分境界で表示上は番号が飛んでも実際の画に抜けがないか確かめる。（公開手順）
- [A168](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/view-source-timecode-in-the-program-monitor.html)　Programのソース時刻表示を有効にしてカットをまたぎ、各カットに使った素材の時刻へ切り替わるか見る。（公開手順）
- [A169](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/change-timecode-display-format.html)　同じ再生位置で時間表示をフレーム番号へ変え、時間表記へ戻した際に同じ画像を指すか確かめる。（公開手順）
- [A170](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/timecode-display-options.html)　時間表示の選択肢を比較し、素材由来の時刻とゼロ起点の経過表示を同じ位置で読み分けられるか試す。（公開手順）
- [A171](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/set-clip-timecode-manually.html)　クリップの開始タイムコードを手入力し、既知のフレームが補正後の時刻で示されるか照合する。（公開手順）
- [A272](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/snap-clips.html)　スナップ有無でクリップ端を再生ヘッドの近くへ動かし、狙ったフレームに揃ったか時刻を比較する。（公開手順）
