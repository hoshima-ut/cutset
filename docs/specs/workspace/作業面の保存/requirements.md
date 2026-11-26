# 作業面の保存の要件（UI-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

パネルのドック・分離・最大化・復元を行い、モニター構成変更後も操作を再開できる。

## 受入条件

ドック、タブ化、分離、最大化、ワークスペース保存・リセット。副画面の取り外しでパネルを主画面に戻し、タイムラインの編集結果と配列の変更を別に管理する。

## 例外と復旧

保存時の副画面がなければ、その画面にあったパネルを主画面の可視領域へ戻す。

## 参照資料と確認項目

- [A041](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/display-premiere-interface-on-a-second-monitor.html)　第2画面へパネルを移し、画面を外すと操作可能な領域へ戻せる。（公開手順）
- [A060](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/what-are-workspaces.html)　起動直後に新規・既存・最近の案件を選び分け、希望する編集画面に入れる。（公開手順）
- [A061](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/import-workspaces.html)　別案件に保存した配列を取り込み、既存のユーザー配列を個別に選択できる。（公開手順）
- [A062](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/change-create-reset-workspaces.html)　新しい配列を保存し、パネルを動かした後で保存時の状態に戻せる。（公開手順）
- [A063](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/manage-workspaces.html)　並べ替え・非表示にしたワークスペースが、切替メニューにも同じ順で現れる。（公開手順）
- [A064](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/display-panel-options-and-menu.html)　パネルのメニューを開き、パネル固有の表示切替が他パネルを変えない。（公開手順）
- [A065](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/navigate-the-panels.html)　タブ切替後の入力フォーカスと再生キーの送り先が一致する。（公開手順）
- [A066](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/dock-group-undock-panels.html)　同じパネルを浮動・分割・タブの各状態に移し、選択中の項目を維持する。（公開手順）
- [A067](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/customize-panels.html)　パネルのサイズと表示を変更し、狭い画面でも選び直しと復元が可能である。（公開手順）
- [A068](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/display-any-panel-full-screen.html)　一つのパネルを最大化して元に戻し、隣のパネル配置と再生位置を照合する。（公開手順）
