# ED-32 トリムの試聴 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

編集点の両側を比較し、フレーム単位またはシャトル操作で変更する。

## 受入条件

同じ場面を複数回ループし、非対称の映像・音声のカット点を独立に直し、Undoする。

## 例外と復旧

試聴区間がシーケンスの外にはみ出す場合は端で短縮する。取消は開始時の境界と再生位置を復元する。

## 参照資料と確認項目

- [A239](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/about-trim-mode.html)　編集点を選んでTrimモードに入り、直前・直後の素材と選択中の編集側を表示から識別できるか試す。（公開手順）
- [A240](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/edit-in-trim-mode.html)　トリムモードでフレーム刻みと複数フレーム刻みを使い、変更量表示と編集後の境界位置を照合する。（公開手順）
- [A241](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/asymmetrical-trimming.html)　映像の終了側と音声の開始側を同時に選んでトリムし、各トラックに意図した方向の変化だけが出るか見る。（公開手順）
- [A242](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-j-k-l-dynamic-trimming-in-trim-mode.html)　Jで逆再生、Lで順再生、Kで停止して同じ編集点を調整し、耳で選んだ位置と確定フレームを照合する。（公開手順）
