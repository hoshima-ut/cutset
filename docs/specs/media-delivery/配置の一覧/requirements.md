# 配置の一覧の要件（IO-18）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

シーケンスの配置を時刻と属性で絞り、該当位置を開く。

## 受入条件

素材名が同じ2カットを時間・トラックで見分け、選んだ方に再生ヘッドが移るか確認。

## 例外と復旧

一覧表示後に配置が削除された場合は行を更新し、同時刻に移動した別配置を開かない。

## 参照資料と確認項目

- [A155](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/navigate-timelines-with-sequence-index.html)　Sequence Indexでオフラインと短いカットを絞り、結果行から正しい位置へ移動しCSVの行とも対応するか確かめる。（26.2でSequence Indexを追加）

## 一覧からの移動とCSV書き出し

現在のシーケンスのクリップを名前・トラックやオフライン状態、短いカットで絞り込む。行を選択すると対応する配置へ移動する。CSVには表示対象となった行と選択した列を指定順で書き出す。
