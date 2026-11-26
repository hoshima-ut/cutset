# 複数案件の共有の要件（IO-35）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

共有ストレージの案件ごとに書込者を一人に定め、別案件の素材を安定参照する。

## 受入条件

編集者Aが案件1を開いたまま、Bは案件1を閲覧し案件2を更新できる。共有先を移した後に同じ素材IDを再接続できる。

## 例外と復旧

書込権が失われたら保存を止め、ローカル変更の退避先を提示する。タイムアウトだけで他者の版を上書きしない。

## 参照資料と確認項目

- [A040](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/best-practices.html)　複数リールの共有案件を用い、素材命名・保存先・バックアップから引き継げる。（公開手順）
- [A714](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/about-productions.html)　1本の長尺番組を撮影・編集の案件に分割し、Productionパネルから両方を開いて役割を区別する。（26.2／26.3で旧Productionsのアップグレード性能を改善）
- [A715](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/create-a-production.html)　新規Productionを共有フォルダーに作成し、別端末から同じ構成を見つけられるか確認する。（公開手順）
- [A716](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/configure-productions-settings.html)　Productionのスクラッチ先を共有用に設定し、2端末が同じ参照先を解決するか確かめる。（公開手順）
- [A717](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/add-projects-to-a-production.html)　既存案件の追加と新規の空案件作成を試し、Production上の名前とディスク上の対応を調べる。（公開手順）
- [A718](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/move-clips-and-sequences-between-projects-in-a-production.html)　シーケンスを別案件へ移動した後、参照する撮影素材を閉じた元案件から正しく解決できるか確認する。（公開手順）
- [A719](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/copy-clips-across-projects-in-a-production.html)　別案件へクリップをコピーし、両案件の項目数・素材ファイル数・元の配置の状態を比較する。（公開手順）
- [A720](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/find-and-edit-source-clips-in-a-production.html)　編集シーケンスから元クリップを表示し、素材を所有する案件と元のタイムコードを特定する。（公開手順）
- [A721](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/how-clips-markers-and-labels-work-in-a-production.html)　同一素材を使う2案件にラベルとマーカーを付け、素材と配置ごとに変更が伝わる範囲を調べる。（公開手順）
- [A732](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/learning-from-broadcast-production.html)　収録・ログ・編集・納品を別担当で引き継ぎ、次担当が素材IDとタイムコードから同じテイクを開けるか測る。（公開手順）
- [A733](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaborate-using-productions/broadcast-workflow-lessons-for-individuals-and-small-teams.html)　一人でも同じ素材を二重整理せず短尺版を再編集できるか、共有ビンと再利用プリセットで試す。（公開手順）
- [A734](https://helpx.adobe.com/premiere/desktop/collaborate-with-others/collaboration-in-premiere.html)　編集権が必要な依頼と視聴コメントだけの依頼を用意し、案件とレビューリンクの選択を使い分けられるか試す。（公開手順）
- [A748](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/networks-and-removable-media-with-digital-video.html)　共有・外付けドライブで編集して取り外し、再接続後に素材IDと案件を復帰する。（障害診断）
