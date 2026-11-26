# ED-49 共有ストレージ上の編集 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

案件単位のロックで複数案件を扱い、案件間の素材参照を保つ。

## 受入条件

案件Aのロックを保ったまま、別端末で案件Bを更新できる。BからAの素材を開いたとき同じIDを解決する。

## 例外と復旧

接続切断でロックの有効性を確認できない場合は共有先への上書きを止め、作業コピーを別に保存できるようにする。

## 参照資料と確認項目

- [A722](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/change-project-lock-status-in-production.html)　書き込む担当者を交代し、ロックアイコンと実際の保存権限が両端末で整合するか確認する。（公開手順）
- [A723](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/collaborate-with-other-teams-and-team-members.html)　部署別に案件を開いて並行作業し、相手の作業中ファイルへの変更要求をどう扱うか確認する。（公開手順）
- [A724](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/server-time-and-productions.html)　サーバーと端末の時刻の差を記録し、保存順・ロック表示の検証時に同じ時刻基準で比較する。（公開手順）
- [A725](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/general-best-practices-for-using-productions-on-shared-storage.html)　共有ストレージから2台で再生・保存し、素材パス、継続転送量、書込み権限の不足を切り分ける。（公開手順）
- [A726](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/storage-vendors-who-have-tested-productions.html)　候補ストレージの機種・構成と公式テスト情報を照合し、社内構成で未検証の組み合わせを明示する。（公開手順）
- [A727](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/productions-faq.html)　共有素材を複製せず旧案件を追加する想定を用意し、FAQに沿って解決できた点と実測が必要な点を記録する。（公開手順）
