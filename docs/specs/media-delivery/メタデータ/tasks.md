# メタデータの作業・試験（IO-19）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-19`、受入IDは `AC-IO-19`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

同一ファイルを案件A・Bで参照する。Aのメモ変更はBに現れず、許可して更新したファイル属性はBの再読込で表示される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [metadata_targets_follow_the_selection](../../../../crates/engine/src/panels_tests.rs#L100) は <code>metadata.get</code> を呼ぶ。
- [edit_original_and_update_metadata_refuse_a_stored_path_media_access_refuses](../../../../crates/engine/src/project_tools/tests.rs#L411) は <code>clip.updateMetadata</code> を呼ぶ。
- [edit_original_update_metadata_and_clip_items](../../../../crates/engine/src/project_tools/tests.rs#L371) は <code>clip.updateMetadata</code> を呼ぶ。

## 素材とタイムラインでiXMLを表示する

- [ ] テイク名と2つのチャンネル名が異なるWAVを2回配置する。素材と両配置で値が一致し、iXMLのないWAVには前の値が残らない。
