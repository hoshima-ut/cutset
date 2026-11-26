# 遠隔モニタリングの要件（IO-50）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

リアルタイムの試聴ストリームを指定先へ送り、遅延・切断を表示する。

## 受入条件

同じ接続方式と対向方式をそれぞれ試し、接続状態、受信映像・音声の時刻を記録する。

## 例外と復旧

未対応方式や対向先の切断時は送出を止め、手元での編集・試聴を継続できる。再接続時に古いフレームを現行として見せない。

## 参照資料と確認項目

- [A668](https://helpx.adobe.com/premiere/desktop/render-and-export/stream-video/overview-of-secure-reliable-transport.html)　映像にフレーム番号と同期音を入れ、SRT受信側で両方が対応するか観察する。（公開手順）
- [A669](https://helpx.adobe.com/premiere/desktop/render-and-export/stream-video/enable-secure-reliable-transport-stream.html)　検証用受信機とのSRT出力を起動・停止し、ローカル再生を維持したまま送信状態が切り替わるか見る。（公開手順）
- [A670](https://helpx.adobe.com/premiere/desktop/render-and-export/stream-video/secure-reliable-transport-modes.html)　CallerとListenerで発呼側を入れ替え、Rendezvousを含め対向設定に応じた接続可否を記録する。（公開手順）
- [A671](https://helpx.adobe.com/premiere/desktop/render-and-export/stream-video/srt-settings.html)　遅延とストリーム識別子を変え、受信側で意図したストリームと遅延を確認する。（公開手順）
