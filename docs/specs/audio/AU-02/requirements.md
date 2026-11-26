# AU-02 音声と映像の同期 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

同期点、時刻、外録音波形などからオフセットを決定し、リンクを調整する。

## 受入条件

口とクラップ音を同期し、選択したタイムコードとチャンネルの保持、解除後の独立移動を確認する。

## 例外と復旧

波形に複数の同期候補があるときは候補を並べ、手動のマーカー指定へ戻れる。ロック中トラックを自動で移動しない。

## 参照資料と確認項目

- [A500](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/link-audio-and-video-clips.html)　外録音声と映像をリンクし、移動・リンク解除・片側移動で選択対象と同期差を確認する。（公開手順）
- [A501](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/synchronize-audio-and-video.html)　カメラ音と外部レコーダーのクラップ音を合わせ、口の動きとクリックの位置を確認する。（公開手順）
- [A502](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/synchronize-clips-in-the-timeline-panel.html)　タイムライン上で同期用マーカーを選んで複数クリップを同期し、各マーカーが同一時刻に揃うか見る。（公開手順）
- [A503](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/merge-clips-in-the-project-panel.html)　Projectで別録りの音と映像を結合し、新しい項目を配置して元の項目が残るか確認する。（公開手順）
- [A504](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/merge-clips-in-the-timeline-panel.html)　既に位置を合わせたタイムライン選択から結合クリップを作り、次の配置でも時間差が再現するか見る。（公開手順）
- [A505](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/use-the-timecode-from-an-audio-primary-clip-to-create-a-merged-clip.html)　外録音声のTCを引き継いだ結合クリップを開き、映像の別TCと区別してソース表示を照合する。（公開手順）
- [A506](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/edit-merged-clips.html)　結合クリップの一部をトリムし、編集後の画と外録音声の対応を前後で確かめる。（公開手順）
- [A507](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/edit-metadata-of-merged-clips.html)　結合項目のメタデータを変更し、構成元素材のどの値を編集したかを再選択して照合する。（公開手順）
- [A508](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/limitations-of-merged-clips.html)　結合クリップで公式に制限される操作を一つ試し、未対応の内容と代替手順の結果を記録する。（公開手順）
