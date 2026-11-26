# 共有案件の公開と同期の要件（IO-34）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

招待した編集者が別端末で版を同期し、同一シーケンスの同時編集を検知する。

## 受入条件

2人が同じシーケンス・別シーケンスを開く。切断→編集→再接続→公開で、未公開版が勝手に置換されないか確認する。

## 例外と復旧

切断中の変更は下書きに残す。同じ配置を別端末で更新していた場合は競合として提示し、合意前に上書きしない。

## 参照資料と確認項目

- [A672](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/about-team-projects.html)　同じTeam Projectを別ユーザーで開き、案件データとローカル素材の可視範囲を別々に確かめる。（公開手順）
- [A673](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/when-to-use-team-projects-and-when-to-use-productions.html)　ネット共有とクラウド案件の2構成で、案件の保管先・素材の配置・変更公開の差を表にする。（公開手順）
- [A674](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/collaboration-using-team-projects.html)　担当者Aが短縮したカットを公開し、担当者Bが更新を受け取って次の作業を始められるか試す。（公開手順）
- [A675](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/create-team-projects.html)　空のTeam Projectに名前と参加者を設定し、再ログインして同じ案件を開けるか確認する。（公開手順）
- [A676](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/create-linked-team-projects.html)　別Team Projectへのリンクを開き、親案件とリンク先の編集対象が区別されるか確認する。（公開手順）
- [A677](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/add-media.html)　担当者Aが追加したテイクを公開し、担当者Bが自分の素材への対応付けを求められるか調べる。（公開手順）
- [A678](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/manage-media.html)　端末ごとに異なる素材ルートを対応付け、一方の再リンクが相手の有効なパスを壊さないか確認する。（公開手順）
- [A679](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/connect-to-team-projects-service.html)　回線を戻してサービスへ再接続し、同期保留中だった案件が一覧のどこに現れるか確認する。（公開手順）
- [A680](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/invite-individual-collaborators-or-groups-to-team-projects.html)　既存案件に検証用アカウントを招待し、宛先と付与された参加範囲を一覧で照合する。（公開手順）
- [A697](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/convert-premiere-projects-to-team-projects.html)　手元の通常案件をTeam Projectに変換し、元案件のコピーと変換後のビン・配置・素材リンクを照合する。（公開手順）
