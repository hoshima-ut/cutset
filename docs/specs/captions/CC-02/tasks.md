# CC-02 字幕の手編集 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CC-02`、受入IDは `AC-CC-02`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

[10,30)の「東京大会」を20で「東京」「大会」に分ける。19では前半、20では後半だけが見え、再結合すると1区間に戻る。

- QA-05　日本語の人名の変換を確定。次に同じ語を対象に発話カットを別操作として試す。 期待結果：字幕校正で変わるのは文言だけ。発話カットは音声・映像・後続位置に与える差を事前表示。Undoで両操作を別々に戻せる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [caption_list_track_filter_never_falls_back_to_every_track](../../../../crates/engine/src/captions/tests.rs#L143) は <code>captions.list</code> を呼ぶ。
- [captions_duplicate_copies_and_overwrites](../../../../crates/engine/src/captions/tests.rs#L318) は <code>captions.duplicate</code> を呼ぶ。
- [set_style_font_style](../../../../crates/engine/src/captions/tests.rs#L379) は <code>captions.setStyle</code> を呼ぶ。
