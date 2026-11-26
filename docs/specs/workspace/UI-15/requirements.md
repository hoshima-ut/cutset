# UI-15 外部入出力の調整 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

音声入出力と映像監視機器の経路・バッファ・同期を確認し、切断を検知する。

## 受入条件

出力先、バッファ、チャンネル割当、外部映像と音の同期を設定する。機器を抜いた後も編集を保存でき、切替先を明示する。

## 例外と復旧

使用中の機器がなくなったら現在の監視を停止して切替先を表示する。録音中なら記録済みの範囲を明示する。

## 参照資料と確認項目

- [A025](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/audio-preferences.html)　同じ波形を再生し、音声設定の変更と配置のゲイン変更を区別する。（公開手順）
- [A026](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/audio-hardware-preferences.html)　入力・出力機器を別々に指定し、収録した信号と試聴した信号を追跡する。（公開手順）
- [A030](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/control-surface-preferences.html)　外部操作面のフェーダーを割り当て、一つの入力で指定トラックだけが動く。（公開手順）
- [A039](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/display-video-on-a-second-monitor.html)　第2画面へ映像のみを出し、主画面でタイムライン操作を続けられる。（公開手順）
- [A782](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/audio-playback-keep-getting-stuck.html)　音声の断続停止を既知のPCM音源で再現し、バッファ変更前後を比較する。（障害診断）
