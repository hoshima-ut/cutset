# IO-08 レイヤー画像 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

統合画像またはレイヤーごとの配置を選び、アルファと寸法を維持する。

## 受入条件

上下2層のPSDを統合版とレイヤー版で読み、下地を重ね、透明領域、編集可能な層数、位置を確認。

## 例外と復旧

未対応の描画モードや効果は、そのレイヤーを示して統合読み込みを選べるようにする。

## 参照資料と確認項目

- [A118](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-photoshop-and-illustrator-files.html)　多層PSDを別々のレイヤーとして扱う場合と統合する場合を比較し、AI形式素材のラスタサイズも点検する。（公開手順）
- [A801](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/import-photoshop-files-into-premiere.html)　透過と複数レイヤーを持つPSDをシーケンスとして読み、背景と文字が分かれた状態で配置されるか見る。（公開手順）
