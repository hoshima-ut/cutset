# 共同作業者管理の要件（ED-47）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

案件への招待と失効を扱い、参加者の素材取得状況と参加権限を区別する。

## 受入条件

二人目を招待し、その端末だけで元メディアを欠落させる。参加は継続し、欠落素材の位置だけを識別できる。

## 例外と復旧

期限切れ招待・権限失効はサーバー側で拒否する。参加継続中に素材が不足した場合は参加者を削除しない。

## 参照資料と確認項目

- [A028](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/collaboration-preferences.html)　共同制作の設定を変えた人と他の参加者で、表示名と編集権限の影響を分ける。（公開手順）
- [A681](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/accept-an-invitation-to-collaborate.html)　招待を承諾した側が対象のTeam Projectを開け、別名の案件へ誤って参加しないか確認する。（公開手順）
- [A682](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/view-online-collaborators.html)　2人目の参加・退出を起こし、オンライン参加者表示と実際の接続状態を見比べる。（公開手順）
- [A683](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/remove-collaborators-from-team-projects.html)　検証用の参加者を削除して再接続し、所有者は編集を継続し、除外した側のアクセスがどう変わるか記録する。（公開手順）
- [A684](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/search-and-filter-team-projects.html)　同名に近い案件を現在・アーカイブに分け、検索条件を変えたときの一覧を照合する。（公開手順）
- [A685](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/archive-team-projects.html)　試験案件をアーカイブし、普段の一覧から消え、アーカイブ一覧で識別可能か確認する。（公開手順）
- [A686](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/delete-archived-team-projects.html)　廃棄用のアーカイブ複製で削除対象名を確認し、キャンセルと実行後の一覧を比較する。（公開手順）
- [A687](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/restore-archived-team-projects.html)　アーカイブした案件を復元し、最後に公開した編集点と参加状態を確認する。（公開手順）
