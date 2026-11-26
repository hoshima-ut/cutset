# IO-52 OTIO交換 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

トラック・配置・素材参照・時間範囲を交換し、表現できない情報を一覧に出す。

## 受入条件

同じ素材の別配置、音先行、空白、複数トラック、マーカーを受け手で開き、1点トリムして戻す。参照動画と素材時刻で照合。

## 例外と復旧

参照先が見つからない場合は配置と尺を残して再リンクを求める。対応しない要素を無言で消去しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html)
- [公開資料 2](https://community.adobe.com/announcements-732/now-released-otio-import-and-export-311699)
