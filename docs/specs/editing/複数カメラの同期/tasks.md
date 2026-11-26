# 複数カメラの同期の作業・試験（ED-37）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-ED-37`、受入IDは `AC-ED-37`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

手拍子がカメラAの100、Bの130、外録の80で鳴る3素材を合わせる。同期位置で音が一つに揃い、遅く始まる角度の先頭不足を表示する。

- QA-06　同期パルスを含む2カメラにメインの別録音を追加。一か所だけ映像アングルを変更。 期待結果：その配置区間の映像だけが変わり、メイン音声のサンプル位置と他の区間が一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [timeline_synchronize_by_audio_and_timecode](../../../../crates/engine/src/multicam_tests.rs#L273) は <code>clip.synchronize</code> を呼ぶ。
- [any_nest_can_be_multicam](../../../../crates/engine/src/multicam_tests.rs#L623) は <code>clip.multicamEnable</code> を呼ぶ。
- [flatten_replaces_with_camera_clips](../../../../crates/engine/src/multicam_tests.rs#L571) は <code>clip.multicamFlatten</code> を呼ぶ。
