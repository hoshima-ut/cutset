# IO-28 監視と操作機器 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

外部画面、音声デバイス、編集コントローラーを識別して各経路を設定する。

## 受入条件

外部ディスプレイと音声機器を選んで映像・クリック音を同期確認。抜線後に代替機器を選び直せるか試す。

## 例外と復旧

抜線した機器を無効として示し、意図しない別の録音入力に切り替えない。再接続後に明示的に再選択できる。

## 参照資料と確認項目

- [A518](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/map-to-audio-output-device-hardware-channels.html)　物理出力の割当先を変更し、ヘッドホンや各スピーカーで指定チャンネルのテスト音を聴く。（公開手順）
- [A632](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/previewing-on-a-television-monitor.html)　外部モニターを指定し、タイムラインと同じフレームのセーフゾーンや画角を比較する。（公開手順）
