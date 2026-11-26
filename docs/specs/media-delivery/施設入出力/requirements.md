# 施設入出力の要件（IO-14）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

映像監視・施設収録の機器と信号形式を列挙し、対応経路で接続する。

## 受入条件

外部機器で作ったファイルを取り込み、画と時刻を照合。出力モニターの選択で収録機器が追加されたように表示しない。

## 例外と復旧

対応しないレートや信号断を区別して表示する。出力専用機器を収録先として選べないようにする。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/previewing-on-a-television-monitor.html)
- [公開資料 2](https://community.adobe.com/announcements-732/now-in-beta-removing-tape-and-capture-workflows-313340)
