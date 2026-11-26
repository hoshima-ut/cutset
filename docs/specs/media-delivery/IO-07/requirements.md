# IO-07 静止画・連番 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

静止画の既定尺と番号付きフレーム列の再生速度・欠番時の挙動を決める。

## 受入条件

桁数を揃えた100枚を25 fpsで読み、単体100枚と4秒の1クリップを区別。途中の欠番を再現ケースにする。

## 例外と復旧

欠番を検出したら該当番号を示し、補間方法を確定するまで番号を勝手に詰めない。

## 参照資料と確認項目

- [A116](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-still-images.html)　透過PNGを読み込み、背景上のアルファと静止画の初期配置尺を確認する。（公開手順）
- [A117](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-images-as-image-sequence.html)　連番画像を一つの動画として読み込み、ファイル番号順とフレーム数を照合する。（公開手順）
- [A119](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/resize-imported-images.html)　高解像度写真をシーケンスに合わせ、元画像を再利用したときに原寸の情報を保持できているか調べる。（公開手順）
