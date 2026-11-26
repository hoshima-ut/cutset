# ED-28 ロールトリム — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

隣接配置の境界だけ動かし、対の合計尺を保つ。

## 受入条件

境界を3フレーム後ろに動かして前側+3、後側−3、後続位置の変更0を照合する。

## 例外と復旧

片側に十分な余白がなくなれば両側を同じ差分で止める。間にギャップがあればロール対象外を示す。

## 参照資料と確認項目

- [A235](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-rolling-edits.html)　ロールで隣接する二つの境界を動かし、増えた尺と減った尺が同じで外側両端が変わらないか試す。（公開手順）
