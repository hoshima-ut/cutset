# 編集中の部分レンダーの要件（UX-08）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

代理素材で作業を続け、変化した区間だけ表示用フレームを更新する。

## 受入条件

出力時に原本へ戻せない場合は不足対象を列挙し、代替画質の使用を選べる。

## 例外と復旧

レンダー完了前に同じ区間が再編集されたら、古い結果を現行版へ採用しない。納品時の原本欠落は配置別に報告する。

## 参照資料と確認項目

- [公開資料 1](https://docs.kdenlive.org/en/project_and_asset_management/project_settings/proxy_settings.html)
- [公開資料 2](https://docs.kdenlive.org/en/user_interface/menu/sequence_menu.html)
