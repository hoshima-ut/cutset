# マーカーの所属と範囲の要件（ED-55）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材マーカーとシーケンスマーカーを区別し、時刻、尺、コメントで探す。

## 受入条件

一つの素材マーカーを異なる位置の2配置で確認し、素材時刻と各シーケンス時刻を混同しない。

## 例外と復旧

素材マーカーがトリムされた範囲の外にある場合はその配置に表示せず、元マーカー自体は保持する。

## 参照資料と確認項目

- [A156](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/overview-of-markers.html)　点のメモと期間を持つメモを作り、マーカーパネルで種類・開始・終了を見分けられるか確認する。（公開手順）
- [A157](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/add-a-marker-to-a-clip.html)　素材の同じ瞬間を使う二つの配置を作り、素材側に加えたマーカーが各配置のどこに現れるか照合する。（26.2で指定長の範囲マーカーを直接作成）
- [A158](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/copy-and-paste-sequence-markers.html)　複数のシーケンスマーカーをコピーし、貼り付け後の位置間隔とコメントが一致するか確認する。（公開手順）
- [A159](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/find-move-and-delete-markers.html)　同名で色の異なるマーカーを検索し、一つを移動してから削除しても他方が元の時刻に残るか調べる。（26.2で名称・コメント・色による検索とジャンプを改善）
- [A160](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/set-default-marker-colors.html)　既定の色を変更して新しいマーカーを付け、既存マーカーの色はその操作で変わらないか確認する。（公開手順）
- [A161](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/show-or-hide-markers-by-color.html)　一色を隠した状態で該当時刻へ移動し、色を再表示すれば元のマーカーが再び現れるか確かめる。（公開手順）
- [A162](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/view-marker-comments.html)　範囲マーカーの名前、説明、長さを変更し、再開後も正しい場所と期間でコメントを開けるか確かめる。（公開手順）
