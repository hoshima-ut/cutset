# IO-23 素材の再リンク — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

欠落した原本の候補を識別情報とともに表示し、確認済み対象を再接続する。

## 受入条件

MacとWindowsでルートが違う複製を用意し、同名・別内容のカメラ素材を誤採用しないか確認。保留を選んだ項目だけを後で接続。

## 例外と復旧

同名・異内容や候補の複数一致は手動確認に戻す。保留した項目を自動で別ファイルに結び付けない。

## 参照資料と確認項目

- [A150](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/locate-and-link-offline-files.html)　移動した素材を案件オープン時に検出し、一つを指定した後に残りの参照がどう復旧したか照合する。（26.2で再リンク探索が改善、26.5で所在指定・オフライン・リセットのコンテキスト操作追加）
- [A151](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/relink-offline-media-automatically.html)　オンラインで使っていた素材の保存場所を変え、再リンク後もタイムラインの各配置と素材時刻が維持されるか確かめる。（26.2で再リンク探索が改善、26.5で所在指定・オフライン・リセットのコンテキスト操作追加）
- [A152](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/manually-locate-and-relink-offline-media.html)　同名で内容が異なる2ファイルを別フォルダーに置き、手動の検索とプレビューで正しい方を明示できるか試す。（26.2で再リンク探索が改善、26.5で所在指定・オフライン・リセットのコンテキスト操作追加）
- [A184](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/create-offline-clips.html)　実ファイルのないプレースホルダーを所定の尺とタイムコードで作り、ビンにオフライン表示されるか確認する。（公開手順）
- [A185](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/edit-offline-clips.html)　未着素材の仮クリップをトリム・並べ替えし、映像が未接続でも配置と仮尺を保存できるか試す。（公開手順）
- [A186](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/relink-offline-clips.html)　後から届いた原本を仮クリップに割り当て、同じ配置位置から指定した素材区間が再生されるか確認する。（公開手順）
- [A187](https://helpx.adobe.com/premiere/desktop/organize-media/ingest-proxy-workflow/convert-online-clips-to-offline-clips.html)　接続中のクリップをオフライン化して、原本を残す操作と実ファイルにも影響する操作の選択肢を確かめる。（公開手順）
- [A746](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/files-conformed-each-time-project-opens.html)　同じ案件を二度開き、最適化ファイルが再利用される条件と権限を確認する。（障害診断）
