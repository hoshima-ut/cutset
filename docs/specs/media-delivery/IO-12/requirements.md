# IO-12 増加中の収録素材 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

追記中のファイルの読める範囲を更新し、確定済みの配置を維持する。

## 受入条件

追記した収録ファイルを再度走査すると末尾だけが伸び、以前に使った先頭の配置時刻は不変。新しい画と音を同じ終端まで再生できる。

## 例外と復旧

書きかけの最終パケットは次回走査まで保留する。ファイルが縮小または交換された場合は自動追記を止める。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/media-preferences.html)
- [公開資料 2](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html)
