# ED-57 検出結果の適用先 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

同じ検出結果を素材注記、サブクリップ、実カットに別々に適用する。

## 受入条件

全選択時にマーカーの数・新規ビンの区間・カット位置を照合。解除してある音声には区間をまたぐ編集点が増えない。

## 例外と復旧

解析時から素材や配置版が変わった場合は適用を止める。採用解除した候補を他の出力先へ自動適用しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/detect-edit-points-using-scene-edit-detection.html)
