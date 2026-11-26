# ロックと連動の要件（ED-13）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

編集禁止と後続を同期移動する指定を分け、複数行に適用する。

## 受入条件

字幕の同期ロック有／無で挿入後の位置を比較。ロックした音楽のクリップ配置が変わらない。

## 例外と復旧

ロックした連動配置を変更しないと成立しない操作では、対象を外すか操作を取り消す判断を明示する。

## 参照資料と確認項目

- [A266](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/sync-lock-to-prevent-changes.html)　同期ロック有無の二つのトラックを用意し、先頭挿入後に各クリップが何フレーム移動したか照合する。（公開手順）
- [A267](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/track-lock-to-prevent-changes.html)　トラックをロックして分割・移動を試し、同時選択した編集可能トラックだけに変更が入るか確認する。（公開手順）
