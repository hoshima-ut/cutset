# 中間素材への置換の要件（IO-33）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

重い配置をレンダー済み素材に置換し、元のソース・効果へ復帰する。

## 受入条件

処理前後と復帰後のタイミング、ハンドル、焼き込んだ効果、引き続き変更できる値を比較する。

## 例外と復旧

生成中断時は元配置を維持する。復帰に必要な原本が欠落したときは再接続を促し、中間素材を保持する。

## 参照資料と確認項目

- [A628](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/render-and-replace-media-in-a-sequence.html)　重い映像をハンドル付きの中間ファイルに置き換え、配置位置と尺を保って再生できるか確認する。（公開手順）
- [A629](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/replace-rendered-clips-with-original-media.html)　置換済みクリップを元へ戻し、焼き込む前の効果のパラメーターが再編集できるか調べる。（公開手順）
