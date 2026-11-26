# UX-12 ブラウザの段階導入 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

共有版の確認から単独編集、複数人編集へ利用可能な操作範囲を拡張する。

## 受入条件

競合するトリム／削除は別案として残し、オフライン再接続時の消失・二重適用を検査する。

## 例外と復旧

オフラインのトリムに対して他端末が配置を削除した場合は競合を残す。再送済み操作は二重適用しない。

## 参照資料と確認項目

- [公開資料 1](https://getartcraft.com/apps/filmcraft)
- [公開資料 2](https://elevate.io/features/collaborative-video-editing)
