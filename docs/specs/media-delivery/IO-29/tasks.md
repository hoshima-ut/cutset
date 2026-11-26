# IO-29 キャッシュ管理 — 作業・試験

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-29`、受入IDは `AC-IO-29`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

波形キャッシュを消し、原本と保存済み案件の内容が同じことを確認する。再度開くと波形だけが再生成される。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [media_cache_cleaning_keeps_the_files_of_the_chosen_folder](../../../../crates/engine/src/settings_tests.rs#L510) は <code>mediaCache.clean</code> を呼ぶ。
- [media_cache_location_policy_and_clean](../../../../crates/engine/src/settings_tests.rs#L459) は <code>mediaCache.clean</code> を呼ぶ。
- 関連する既存テストモジュール：[crates/engine/src/perf.rs](../../../../crates/engine/src/perf.rs)。
