# ビンと絵コンテの要件（ED-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

自由配置の順序、並べ替え、実際のタイムライン上の順番を独立させる。

## 受入条件

同じ素材群を複数のレイアウトで整理し、並び替えても既存編集の順序が変わらない。

## 例外と復旧

ソートキーが同じ素材は安定した順序で表示し、表示方式を変更しても選択済みの項目を別項目に置換しない。

## 参照資料と確認項目

- [A072](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customization-options-for-the-project-panel.html)　同じビンをリスト・アイコン・自由配置で開き、項目数と元素材への参照が一致するか確かめる。（公開手順）
- [A073](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customize-icon-view-in-project-panel.html)　アイコンの大きさと代表フレームを変え、指定したテイクをサムネイルで見分けられるか確かめる。（公開手順）
- [A074](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customize-metadata-in-freeform-view-in-project-panel.html)　自由配置したカードの表示項目を撮影日とカメラ名に切り替え、該当する素材の値が表示されるか確認する。（公開手順）
- [A075](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customize-freeform-view-in-project-panel.html)　素材カードを任意位置に移動・重ね、再び自由配置表示に戻ったときに絵コンテの並びを確認する。（公開手順）
- [A076](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customize-list-view-in-project-panel.html)　リスト表示で列順と列幅を変え、狭いパネルでもテイク番号と尺を並べて読めるか試す。（公開手順）
- [A077](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/align-and-reset-clips-to-grid-in-freeform-view-in-project-panel.html)　ばらばらに置いたカードをグリッド整列し、位置のリセット後に手動配置がどう変わるか確認する。（公開手順）
- [A078](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/create-layouts-in-freeform-view-in-project-panel.html)　同じ素材から取材順と採用順の二つのレイアウトを保存し、それぞれの順序を呼び戻せるか試す。（公開手順）
- [A079](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/customize-the-position-of-the-project-panel.html)　Projectパネルを別のドックへ移して、同じビンからタイムラインへ引き続き素材を置けるか確認する。（公開手順）
- [A080](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/list-view-columns.html)　一覧にフレームレートと音声情報の列を加え、24fpsの無音素材と30fpsの有音素材を識別できるか試す。（公開手順）
- [A081](https://helpx.adobe.com/premiere/desktop/get-started/customize-the-project-panel/restore-or-delete-layouts-in-freeform-view-in-project-panel.html)　保存済みレイアウトを復元してから一つを削除し、残るレイアウトとビン内の素材数を照合する。（公開手順）
