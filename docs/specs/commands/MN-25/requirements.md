# MN-25 レイアウトの管理 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

パネル配置を名前付き保存し、位置が崩れたとき復元する。

## 受入条件

パネルを浮動化して試し、リセットで保存レイアウトを復元。編集内容・再生位置へ影響しないことを確認。

## 例外と復旧

保存時の外部ディスプレイが無い場合は利用可能な画面内に戻す。存在しない拡張パネルは他のパネルの復元を妨げない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/change-create-reset-workspaces.html)
