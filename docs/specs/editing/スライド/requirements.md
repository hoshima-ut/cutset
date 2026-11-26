# スライドの要件（ED-30）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

中央配置の内容と尺を保ち、両隣の端を調整して移動させる。

## 受入条件

中央を3フレーム後ろに移動して、前後外端と全体尺が一致する。

## 例外と復旧

隣の配置がない、または必要な側がロックされている場合は3者を変更しない。

## 参照資料と確認項目

- [A237](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-slide-edits.html)　スライドで中央クリップを移し、中央素材範囲を維持して前後の外端と全体尺が一致するか確認する。（公開手順）
