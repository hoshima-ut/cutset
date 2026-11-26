# 外部字幕と翻訳の作業・試験（CC-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-CC-03`、受入IDは `AC-CC-03`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

1.000〜2.000秒の日本語字幕を取り込み英語トラックに翻訳する。英語側の人名を修正し、2つのトラックを個別表示しても日本語の原文と時刻は変わらない。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [caption_export_warns_about_characters_608_and_708_cannot_carry](../../../../crates/engine/src/captions/tests.rs#L418) は <code>captions.export</code> を呼ぶ。
- [caption_track_language_survives_import_and_ttml_export](../../../../crates/engine/src/captions/tests.rs#L392) は <code>captions.export</code> を呼ぶ。
- [captions_import_edit_export_and_burn_in](../../../../crates/engine/src/captions/tests.rs#L14) は <code>captions.export</code> を呼ぶ。
