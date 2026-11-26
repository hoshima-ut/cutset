# ED-38 カメラ切替編集 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-38`、受入IDは `AC-ED-38`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

25と50でA→B→Aに切り替え、外録音を固定する。映像は3区間、音声は元と同じ長さ・タイミングで切替点のサンプルも連続する。

- QA-06　同期パルスを含む2カメラにメインの別録音を追加。一か所だけ映像アングルを変更。 期待結果：その配置区間の映像だけが変わり、メイン音声のサンプル位置と他の区間が一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [edit_cameras_and_save_load](../../../../crates/engine/src/multicam_tests.rs#L600) は <code>multicam.editCameras</code> を呼ぶ。
- [grid_pages_decode_only_their_angles_at_reduced_resolution](../../../../crates/engine/src/multicam_tests.rs#L781) は <code>multicam.grid</code> を呼ぶ。
- [more_than_sixteen_angles_page_and_switch](../../../../crates/engine/src/multicam_tests.rs#L731) は <code>multicam.page</code> を呼ぶ。
