# ED-22 配置・マーカー検索 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

配置と素材・シーケンスの注記を絞って一致時刻に移る。

## 受入条件

同じ素材を2回使用して素材側の印を照合。名称が同じ別配置はトラックとタイムコードで選ぶ。

## 例外と復旧

再検索前に配置が削除された結果は無効と表示し、同じ名前の別配置を代用しない。

## 参照資料と確認項目

- [A269](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/find-clips-in-a-sequence.html)　同じ素材が3回現れるシーケンスで次の一致へ移動し、それぞれの配置時刻を取り出せるか試す。（公開手順）
