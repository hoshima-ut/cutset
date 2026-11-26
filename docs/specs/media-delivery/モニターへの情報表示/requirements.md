# モニターへの情報表示の要件（IO-20）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材時刻・名称・選択角度などを試聴映像に重ね、書き出し設定とは独立させる。

## 受入条件

モニター表示を切り替え、確認用表示が納品動画へ意図せず焼き込まれないことを確認。

## 例外と復旧

時刻が取得できない素材は未取得と表示し、直前の素材の時刻を表示し続けない。

## 参照資料と確認項目

- [A101](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/display-metadata-as-overlays.html)　同一フレームに素材名とソース時刻を重ね、実際に表示している素材と値が合うか確認する。（公開手順）
- [A102](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/set-overlay-settings.html)　左右に別のメタデータを配置して文字サイズを変え、表示設定を呼び戻した際の項目と位置を確かめる。（公開手順）
- [A197](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/display-metadata-as-overlays.html)　メタデータ項目を映像上で確認してカットをまたぎ、直前のクリップの値が次の映像に残らないか見る。（公開手順）
- [A198](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/display-overlays-in-multi-camera-view.html)　マルチカメラ表示で各角度名を重ね、カメラ順を並べ替えた後もラベルが正しい映像に付くか確かめる。（公開手順）
- [A199](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/create-overlay-settings.html)　撮影者名とタイムコードを異なる位置に置いた表示セットを作り、別の素材でも同じ位置関係になるか試す。（公開手順）
- [A200](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/overlay-settings-reference.html)　オーバーレイの配置・背景等を変えて読みやすさを比較し、画面の値が書き出し映像に混入しないか確認する。（公開手順）
- [A201](https://helpx.adobe.com/premiere/desktop/organize-media/edit-metadata/import-export-or-delete-overlay-settings.html)　オーバーレイプリセットを書き出して別環境へ取り込み、削除後も他のユーザープリセットが使えるか確かめる。（公開手順）
