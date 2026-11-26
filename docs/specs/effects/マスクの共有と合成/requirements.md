# マスクの共有と合成の要件（FX-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

マスクを複写・再割当し、重なる領域を和・差で組み合わせる。

## 受入条件

穴のある領域を作り、一方の輪郭だけを移して対象効果を照合する。

## 例外と復旧

参照先が削除された場合は該当する効果に欠落を表示する。別の同名マスクへ自動で割り当てない。

## 参照資料と確認項目

- [A484](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/refining-and-combining-masks.html)　二つの輪郭を足し引きしてドーナツ状の領域を作り、中心が処理から外れるか確認する。（公開手順）
- [A485](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/apply-effects-to-existing-unassigned-masks.html)　未割り当ての輪郭に後から色補正を割り当て、元の輪郭と範囲が一致するか見る。（公開手順）
- [A486](https://helpx.adobe.com/premiere/desktop/add-video-effects/work-with-masks/copy-and-paste-masks.html)　ある効果のマスクを別効果へコピーまたは移動し、元側に残る個数と宛先の輪郭を比較する。（公開手順）
