# メタデータの要件（IO-19）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

ファイルのメタデータと案件内属性を別々に読み書きし、対象を明示する。

## 受入条件

同じファイルを別案件に取り込み、案件ローカルの記述と元データに書いた記述がどちらに現れるか照合。読取専用ファイルでも取り込み可能か確認。

## 例外と復旧

参照元が読取専用ならファイル属性の書込を無効にする。案件メモの編集と素材の読み込みは継続できる。

## 参照資料と確認項目

- [A189](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/metadata-in-premiere.html)　同じ撮影素材のファイル属性と案件内で付けた説明を別々に変更し、どちらが他案件へ引き継がれるか確認する。（公開手順）
- [A190](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/edit-xmp-metadata.html)　書き込み可能な試験素材にXMP項目を設定し、別の対応読取ツールから値と保存場所を照合する。（公開手順）
- [A191](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/search-xmp-metadata.html)　Metadataパネルの検索で多数の項目から撮影地だけを絞り、検索解除で他の項目を再表示できるか試す。（公開手順）
- [A192](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/show-or-hide-metadata-in-premiere.html)　使わないメタデータ列を非表示にして再表示し、入力済みの値自体は失われていないか確認する。（公開手順）
- [A193](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/save-switch-or-delete-metadata-sets.html)　取材用と納品用の項目セットを保存し、一方だけを削除しても他方の表示設定が残るか試す。（公開手順）
- [A194](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/create-metadata-schemas-and-properties.html)　新しいスキーマに独自項目を加え、同名の既存項目と混ざらず型に沿った値が記録されるか確認する。（公開手順）
- [A195](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/view-clip-data-in-the-metadata-panel.html)　同じファイルを参照する別のクリップを順に選び、クリップ固有の説明が正しい項目に表示されるか見る。（公開手順）
- [A196](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/link-clip-data-to-xmp-metadata.html)　クリップ項目とXMP項目を連動させた状態で値を更新し、連動を解除した場合との差を再読込後に照合する。（公開手順）

<a id="premiere-27-17"></a>

## 素材とタイムラインでiXMLを表示する（27.0との照合）

録音ファイルから取得したiXMLを素材IDに結び付け、素材モニターと各配置から参照する。[Adobeの公開資料](https://helpx.adobe.com/jp/premiere/desktop/get-started/preferences-and-settings/media-preferences.html)に対応するCutsetの操作条件を、[設計](design.md#premiere-27-17)と[受入試験](tasks.md#premiere-27-17)に記載する。
