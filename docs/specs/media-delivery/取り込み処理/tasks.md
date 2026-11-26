# 取り込み処理の作業・試験（IO-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-04`、受入IDは `AC-IO-04`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

検証コピーの途中で出力先を満杯にする。空き容量を確保して再試行し、コピー完了後にカードを外しても同じ素材を一度だけ読み戻せる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [a_failed_file_import_still_reports_the_empty_folders](../../../../crates/engine/src/media_browser_tests.rs#L429) は <code>mediaBrowser.import</code> を呼ぶ。
- [every_interchange_document_the_importer_reads_is_listed](../../../../crates/engine/src/media_browser_tests.rs#L380) は <code>mediaBrowser.list</code> を呼ぶ。
- [favorites_add_and_remove](../../../../crates/engine/src/media_browser_tests.rs#L186) は <code>mediaBrowser.favorite</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/media_browser.rs](../../../../crates/engine/src/media_browser.rs)。
