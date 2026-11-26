# ED-21 配置の置換と属性 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

位置を維持した素材差し替えと、選択属性の貼り付けまたは無効化を行う。

## 受入条件

既存の尺・効果・音声のどれが残るか比較し、無効化を戻せば元配置が再び出力される。

## 例外と復旧

新しい素材の余白が足りなければ不足する側と尺を提示し、利用者が調整するまで元の配置を保つ。

## 参照資料と確認項目

- [A273](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/enable-or-disable-a-clip.html)　配置を無効化して同位置の下層が見え、再び有効化すると元のテイクと編集長が戻るか見る。（公開手順）
