# ED-48 シーケンスの共同編集 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

編集者・基準版・ロックを可視化し、公開と受信を別操作にする。

## 受入条件

二端末で同じ基準版から編集し、一方が先に確定する。後の変更は競合として提示され、先の変更を失わない。

## 例外と復旧

古い基準版の変更は対象と競合範囲を返し、他者の確定編集も未公開のローカル案も破棄しない。

## 参照資料と確認項目

- [A688](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/publish-an-edited-sequence-with-changes.html)　未公開の1カットを残して変更を公開し、公開対象と共同編集者が実際に読み込む版を比べる。（公開手順）
- [A689](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/visual-cues-during-collaboration.html)　編集・更新待ち・読取専用の状態を2端末で作り、ユーザー名とアイコンの意味を照合する。（公開手順）
- [A690](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/offline-editing-and-cloud-sync-status.html)　切断中の編集を保存し、再接続後にクラウド表示と未送信項目が整合するか確認する。（公開手順）
- [A691](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/view-versions-of-a-team-project.html)　2回の公開に異なる変更説明を付け、版一覧からどの修正がいつ公開されたか特定する。（公開手順）
- [A692](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/create-a-new-team-project-from-a-version.html)　過去の版から新案件を作り、元案件の最新版と新案件の古いカット点をそれぞれ再生して区別する。（公開手順）
- [A693](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/specify-auto-save-cache-location.html)　自動保存キャッシュの場所を別ボリュームへ変え、以降の保存の生成先と再開時の参照先を確認する。（公開手順）
- [A694](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/sequence-locking.html)　同時に同じシーケンスを開き、一方がトリム中のもう一方に所有者・閲覧状態が示されるか調べる。（公開手順）
- [A695](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-team-projects/sequence-locking-for-offline-editing.html)　ロック取得後に担当者を切断し、別担当者が編集した場合の復帰時の扱いを記録する。（公開手順）
