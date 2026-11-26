# Rustでマーカー追加とUndoを追う

タイムラインにマーカーを一つ追加し、Undoで元に戻す処理を読みます。追うのは「入力を受け取る関数」「案件を書き換える箇所」「履歴を確定する箇所」の三つです。コードを読むだけならビルドは不要です。

編集者から見た動作は[マーカーの仕様](../specs/editing/ED-55/requirements.md)と[Undo・Redoの仕様](../specs/editing/ED-45/requirements.md)にあります。他の機能を調べるときは[ディレクトリ案内](repository-map.md)から担当パッケージを探せます。

## 最初に開くファイル

Cutsetは、複数のパッケージをCargoのワークスペースにまとめています。ここではCLIのパッケージ `filmcraft-cli`、編集を実行する `filmcraft-engine`、案件の型を定義する `filmcraft-project` を使います。Rustのコンパイル単位をクレートと呼びます。この例ではCLIの起点が `src/main.rs`、ライブラリの起点が `src/lib.rs` です。依存関係は各パッケージの `Cargo.toml` にあります。コードに現れる `filmcraft_project` はパッケージ名のハイフンをアンダースコアにした名前です。[ワークスペース](../../Cargo.toml) ・ [CLIのパッケージ定義](../../apps/filmcraft-cli/Cargo.toml) ・ [エンジンのパッケージ定義](../../crates/engine/Cargo.toml)

| 順番 | ファイル | エディタで探す文字列 | 読むポイント |
| --- | --- | --- | --- |
| 1 | [試験入力](../verification/fixtures/marker-history.jsonl) | `markers.add` | 誰が何を要求しているか |
| 2 | [CLI](../../apps/filmcraft-cli/src/main.rs) | `async fn cli_run`、`impl Backend` | 同じセッションに命令を順番に渡す箇所 |
| 3 | [エンジン](../../crates/engine/src/lib.rs) | `pub fn execute(` | 命令IDから実行する関数を引く箇所 |
| 4 | [命令定義](../../crates/engine/src/commands.rs) | `"Add Marker"` | 名前と時刻を取り出し、マーカーを追加する箇所 |
| 5 | [シーケンス](../../crates/project/src/sequence.rs)・[マーカー](../../crates/project/src/track.rs) | `pub struct Sequence`、`pub struct Marker` | 追加したデータを保持する型 |
| 6 | [エンジン](../../crates/engine/src/lib.rs) | `pub fn edit<R>`、`pub fn undo(` | 新しい案件を確定する箇所と以前の案件へ戻す箇所 |

### 1. CLIから関数へ

試験入力の2行目は、時刻0に `Cutset spec check` という名前を付ける命令です。`cli_run` はループの手前で一度だけ `Backend::open` を呼びます。`--demo` で起動した場合はデモ案件を開き、同じ `Session` でスクリプトの各行を処理します。`enum Backend` には `Local` と `Bridge` があり、`match self` が今の値に対応する分岐を選びます。この例は `Backend::Local(s)` から `s.execute(id, params)` を呼ぶ経路です。[CLI](../../apps/filmcraft-cli/src/main.rs)

```rust
pub fn execute(&mut self, id: &str, params: Value) -> Result<Value>
```

この関数の `&mut self` は呼び出し中にセッションを変更できる借用、`&str` は呼び出し元の文字列を読むための借用です。`params: Value` はJSON値を所有権ごと受け取ります。戻り値の `Result<Value>` は、このクレートでは成功の `Ok(Value)` と失敗の `Err(EngineError)` のどちらかです。実装は `commands::find(id)` で定義を取得し、実行条件を調べ、`(spec.run)(self, &params)` で登録された関数を呼びます。関数側はJSONを借りて読めます。[Session::execute と Result の型定義](../../crates/engine/src/lib.rs)

### 2. JSONからマーカーへ

`"Add Marker"` の `cmd!(...)` は命令の登録マクロです。`!` がマクロ呼び出しの印です。末尾の `|s, p| { ... }` が実行する関数（クロージャ）で、`s` はセッション、`p` は引数のJSONです。まず `source_monitor::route` が対象を調べます。試験入力の `"target":"program"` では `Ok(None)` が返り、続くシーケンス編集へ進みます。[命令定義](../../crates/engine/src/commands.rs) ・ [対象の振り分け](../../crates/engine/src/source_monitor.rs)

```rust
let t = sequence_time_p(s, p, "", "markers.add")?.unwrap_or(ph);
```

この一行で、負の時刻、時刻の省略、0以上の時刻を区別しています。`sequence_time_p` の型は `Result<Option<Tick>>` です。`?` は外側の `Err` を呼び出し元へ返し、成功時には内側の `Option` を取り出します。`unwrap_or(ph)` は `Some(t)` なら指定時刻、`None` なら再生ヘッドの位置を選びます。負の時刻を渡すと、マーカーを追加する前にエラーが返ります。[時刻の解釈とマーカー命令](../../crates/engine/src/commands.rs)

追加処理は `s.edit_sequence("Add Marker", |q, ctx, _| { ... })` の中です。`q` は変更できる `Sequence`、`ctx` は新しいIDを発行できる編集用の値、`_` はこの処理で使わない引数です。`q.markers` の型は `Vec<Marker>`（可変長の配列）です。`push` して開始時刻順に並べ、割り当てたIDを返します。名前が元のJSONより長く生きられるのは、`to_string()` が所有する `String` を作り、その所有権を `Marker` に渡すためです。[追加処理](../../crates/engine/src/commands.rs) ・ [Sequence](../../crates/project/src/sequence.rs) ・ [Marker](../../crates/project/src/track.rs)

### 3. 履歴を確定し、Undoする

`Session::edit_sequence` から `edit_sequence_as`、今回の分岐では `edit` へ進みます。`edit_sequence<R>` の `R` は編集処理が返す値の型で、今回は `MarkerId` です。引数の `impl FnOnce(...)` は「渡された処理を一度呼び出せる」というトレイトの条件です。登録側はマーカー固有の変更を書き、エンジン側がコピー上でその変更を実行し、シーケンスを検査します。[Session::edit_sequence と Session::edit](../../crates/engine/src/lib.rs)

`edit` は変更に成功すると、現在の案件を新しい案件に差し替え、以前の案件をUndo履歴に積み、Redo履歴を空にします。案件は `Arc<Project>` で保持しています。`Arc` は複数の所有者が同じ値を共有するための型です。`edit.undo` の登録先から `Session::undo` を開き、`self.history.undo.pop()?` を探してください。ここでの戻り値は `Option<String>` なので、履歴が空なら `?` が `None` を返します。履歴があれば以前の案件に差し替え、取り消した案件をRedo履歴に積み、操作名を返します。[Undoの命令定義](../../crates/engine/src/commands.rs) ・ [履歴の更新](../../crates/engine/src/lib.rs)

## 読んだ結果を確かめる

リポジトリ直下で実行します。最初のビルドでは依存関係の取得とコンパイルに時間がかかります。`-p` で対象パッケージを選び、`--` の後にCLIの引数を渡します。[開発環境の準備](rust.md)

```sh
cargo run --locked --release -p filmcraft-cli -- --demo run docs/verification/fixtures/marker-history.jsonl
```

結果は1行1命令です。`sequence.inspect` の4行を比較します。デモ案件のマーカー数は最初が4、追加後が5、Undo後が4、Redo後が5です。Undoの応答は `{"undone":"Add Marker"}` です。シーケンス全体が元に戻ったかは、開始時とUndo後の `result` を比較してください。[自動比較する手順](../verification/marker-history.md)

次に、追加時刻を負にしたら、どの行でエラーが返るか予想してください。次のコマンドはエラー終了し、`time must not be negative` を表示します。

```sh
cargo run --locked --release -p filmcraft-cli -- --demo exec markers.add frame=-1
```

テストでも同じ境界を確認できます。`negative_place_and_marker_times_are_refused` はエラーに加え、失敗後の案件が変更前と等しいことを検査します。`undo_steps_keep_the_command_that_made_them` はUndoとRedoで命令IDが正しい履歴に移ることを調べます。`#[test]` はテスト関数の目印、`assert_eq!` は二つの値が等しいという期待です。一件だけ実行する場合は次のように対象を絞れます。[負の時刻のテスト](../../crates/engine/src/tests.rs) ・ [履歴のテスト](../../crates/engine/src/history_tests.rs)

```sh
cargo test --locked --release -p filmcraft-engine --lib history_tests::undo_steps_keep_the_command_that_made_them -- --exact
```

次の練習では、同じ命令に `"target":"source"` を渡し、素材にマーカーを付ける経路を読んでください。`route` がソース素材を要求する場所と、素材を開いていない場合に返すエラーを見つけたら、シーケンスを編集した経路との違いを説明できます。[ソースモニターの実装とテスト](../../crates/engine/src/source_monitor.rs)

最終確認日 2026-11-26
