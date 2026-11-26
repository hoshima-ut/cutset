# 素材・完成版の文字起こしの要件（ED-41）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

言語、範囲、話者を指定し、発言と元の音声区間を結び付ける。

## 受入条件

カメラ音声と外部マイクを別チャンネルに持つ素材で、選んだチャンネルの発言に移動する。

## 例外と復旧

選択した認識モデルが未導入なら対象言語と必要な取得手順を示す。解析失敗時に旧文字起こしを消去しない。

## 参照資料と確認項目

- [A034](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/transcription-preferences.html)　解析と文字起こしの自動開始を個別に設定し、同じ素材を二重処理しないか確認する。（公開手順）
- [A223](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/transcribe-video.html)　日本語の短い取材映像を文字起こしし、語句を選んだとき元の発話時刻へ移動できるか確かめる。（26.2で話者判定等、26.5で発声検出モデルを改善）
- [A224](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/edit-transcripts-using-text-based-editing.html)　固有名詞の誤認識だけを修正し、素材とシーケンスの尺・切れ目が変更されていないか確認する。（公開手順）
- [A226](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/transcribe-individual-source-files.html)　一つのソースファイルを先に文字起こしし、その同じ発話を別シーケンスへ使って原音と照合する。（26.2で話者判定等、26.5で発声検出モデルを改善）
- [A227](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-video-using-text-based-editing/edit-speaker-names-in-transcription.html)　仮の話者名を実名へ変更し、同じ話者の複数発言と別の話者のラベルを比較する。（公開手順）
- [A377](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/languages-supported-by-speech-to-text.html)　実際に使う二言語を言語選択一覧と照合し、選択した言語の短い音声で認識結果を試す。（公開手順）
