# Cutsetのディレクトリ案内

2026-11-26時点。画面の起動は `apps/`、編集の本体は `crates/`、実装する振る舞いと受入条件は `docs/specs/` から読めます。CutsetはFilmCraftのforkなので、Rustのパッケージ名や実行ファイル名には `filmcraft` が残っています。Cargoは、関連する複数のパッケージを一つのワークスペースとして扱います。このリポジトリではアプリ3個、`crates/` 配下31個、開発用の `xtask` 1個が対象です。[Cargoのワークスペース定義](../../Cargo.toml)

最初の一例として、[Rustでマーカー追加とUndoを追う](reading-rust.md)では、この表のCLI、エンジン、案件データを順に開きます。

## 何を調べたいかで入口を選ぶ

| 調べたいこと | 開く順番 |
| --- | --- |
| タイムラインで受けた操作が案件にどう反映されるか | [パネル](../../crates/ui-egui/src/panels) → [エンジンの命令登録](../../crates/engine/src/commands.rs) → [編集処理](../../crates/edit/src/lib.rs) → [案件の型](../../crates/project/src/lib.rs) |
| 画面なしで同じ命令を試したい | [CLIの引数](../../apps/filmcraft-cli/src/args.rs) → [CLIの分岐](../../apps/filmcraft-cli/src/main.rs) → [エンジン](../../crates/engine/src/lib.rs) |
| 別の編集ソフトにタイムラインを渡したい | [機能索引](../specs/index.md)で対象形式を選ぶ → [交換形式の実装](../../crates/interchange/src/lib.rs)で読み書きの入口を調べる。動画ファイルへの書き出しは[出力処理](../../crates/export/src/lib.rs)を読む。 |
| AIから編集機能を使いたい | [CutsetのAI接続設計](../architecture/model-connections.md)で要件を確認し、[既存のMCPサーバー](../../crates/automation/src/lib.rs)で編集命令を呼び出す経路を読む。 |
| ブラウザで素材を開く仕組みを知りたい | [Webアプリ](../../apps/filmcraft-web/README.md) → [ブラウザの入力処理](../../apps/filmcraft-web/src/import.rs) → [ブラウザ用の保存処理](../../apps/filmcraft-web/src/opfs.rs) |

## ルート直下の全ディレクトリ

| 場所 | 中にあるもの |
| --- | --- |
| [apps/](../../apps) | 3種類の起動口。`filmcraft/` は[デスクトップ](../../apps/filmcraft/src/main.rs)、`filmcraft-cli/` は[端末](../../apps/filmcraft-cli/src/main.rs)、`filmcraft-web/` は[WebAssembly](../../apps/filmcraft-web/src/lib.rs)。Web版の `web/` は配信用HTMLなど、`tests/` はブラウザ等のテスト。 |
| [crates/](../../crates) | 本体のソース。パッケージごとに `Cargo.toml` があり、ライブラリの `src/lib.rs` から公開する型やモジュールを辿れる。後述の表に全31個を収録。 |
| [docs/](../README.md) | 製品仕様、設計、開発手順、検証記録。目的ごとの内訳は次の表。 |
| [tools/](../../tools) | Cutsetの開発用スクリプト。仕様と作業を結ぶ[ハーネス](../../tools/cutset_harness.py)、[仕様台帳の検査](../../tools/check_catalog_links.py)、[秘密情報の検査](../../tools/secret-guard)など。`fixtures/` に試聴計画のテスト入力がある。 |
| [xtask/](../../xtask/src/main.rs) | Cargoから呼ぶRust製の開発ツール。素材の帰属情報を検査する `cargo xtask assets` やWebビルドなどの分岐が `src/main.rs` にある。 |
| [assets/](../../assets/README.md) | `app-icon/` に配布用アイコン、`fonts/` に同梱フォントとライセンス。素材単位の帰属情報は `.attribution`、一覧は[帰属表示](../../ATTRIBUTION.md)。 |
| [contributors/](../../contributors) | 表示用の寄稿者データ。`people.toml` に表示名、`contributors.json` に上流リポジトリの集計データがある。 |
| [packaging/](../../packaging) | `macos/` はアプリとDMG、`windows/` はインストーラー、`linux/` と `freebsd/` は各OSの配布物、`web/` は静的サイトの配布設定。ブラウザ用アプリ本体は `apps/filmcraft-web/`。 |
| [.cargo/](../../.cargo/config.toml) | `cargo xtask` を `xtask` パッケージの実行に結び付けるCargo設定。 |
| [.config/](../../.config/nextest.toml) | Rustのテストランナーnextestの設定。GPUや実時間計測を使うテストの並列実行を調整する。 |
| [.githooks/](../../.githooks) | コミットとpushの直前に秘密情報を検査するGitフック。[導入手順](../security/credentials.md) |
| [.github/](../../.github) | `ISSUE_TEMPLATE/` は問い合わせの様式、`workflows/` は上流から継承したテスト・配布の定義。CutsetのGitHub Actionsは停止中で、開発時の検証はローカルで行う。 |

## docsの内訳

| 場所 | 読む場面 |
| --- | --- |
| [specs/](../specs/README.md) | 編集者の操作や受入条件を調べるとき。分野別の `機能ID/requirements.md`、`design.md`、`tasks.md` を順に読み、機械検証用の台帳は `data/` で見る。 |
| [architecture/](../architecture) | 製品全体の境界、エンジン、編集対象の関係を調べるとき。編集操作で何が影響を受けるかは[編集グラフ](../architecture/edit-graph.md)から読める。 |
| [adr/](../adr/0001-platform-ffi.md) | 設計判断の理由を調べるとき。OS固有APIを呼び出すコードをどこに許すかを記録している。 |
| [development/](README.md) | 実装やレビューに参加するとき。ハンドブック、マイルストーン、開発の引継ぎを置く。 |
| [verification/](../verification/coverage.md) | 仕様を実際にどこまで確かめたか調べるとき。検証手順と入力例の `fixtures/` がある。 |
| [security/](../security/credentials.md) | 認証情報の保存・混入防止・流出時対応を確認するとき。 |
| [reference/filmcraft/](../reference/filmcraft/README.md) | 継承したFilmCraftの制御プロトコル、ファイル形式、既存操作を確認するとき。 |
| [brand/](../brand/LICENSE-brand.txt) | 上流のブランド標章に適用される条件を確認するとき。 |

## cratesの内訳

表中のリンクは各パッケージの入口です。`pub use` だけのファイルは別パッケージの型や関数を公開し直しています。`craft_…` の実装がこのツリーに見つからないときは、ルートの[依存先と固定リビジョン](../../Cargo.toml)から上流を調べます。

| 関心のある領域 | パッケージと役割 |
| --- | --- |
| 編集と保存 | [project](../../crates/project/src/lib.rs) は案件・シーケンス・トラックなどのデータ型。[edit](../../crates/edit/src/lib.rs) は挿入やリップルなどのタイムライン演算。[engine](../../crates/engine/src/lib.rs) は編集セッション、コマンド、履歴。[format](../../crates/format/src/lib.rs) は `.fcproj` の読み書き、移行、自動保存。 |
| 画面・自動操作・OS | [ui-egui](../../crates/ui-egui/src/lib.rs) はパネル、タイムライン、モニター。[automation](../../crates/automation/src/lib.rs) はMCPと起動中のアプリへの接続。[platform](../../crates/platform/src/lib.rs) はOSのハードウェア映像処理。 |
| 時間・座標・色・フレーム | [time](../../crates/time/src/lib.rs) は時間とタイムコード。[geom](../../crates/geom/src/lib.rs) は点・矩形・座標変換。[color](../../crates/color/src/lib.rs) は色変換やLUT。[frame](../../crates/frame/src/lib.rs) は映像フレームと音声バッファの表現。 |
| 素材の読み込み | [media](../../crates/media/src/lib.rs) は映像・音声の取得口、キャッシュ、静止画や生成素材。[codecs](../../crates/codecs/src/lib.rs) はコンテナとデコーダーの選択、シーク。[dng](../../crates/dng/src/lib.rs) はカメラRAW画像の復号。 |
| バイナリ形式 | [bitstream](../../crates/bitstream/src/lib.rs) はビット単位の読み書き。[isobmff](../../crates/isobmff/src/lib.rs) はMP4/MOV、[matroska](../../crates/matroska/src/lib.rs) はMKV/WebM、[cfb](../../crates/cfb/src/lib.rs) はAAFにも使う複合ファイル形式。いずれも共有ライブラリの実装を公開する入口。 |
| 描画・計測・納品 | [render](../../crates/render/src/lib.rs) はシーケンスを評価して合成するCPU実装。[gpu](../../crates/gpu/src/lib.rs) はGPU合成。[scopes](../../crates/scopes/src/lib.rs) は波形やヒストグラムの計算。[export](../../crates/export/src/lib.rs) はレンダー、符号化、ファイル出力。[interchange](../../crates/interchange/src/lib.rs) は他の編集ツールとやり取りするタイムラインの変換。 |
| 文字と字幕 | [text](../../crates/text/src/lib.rs) はフォント、文字組み、ラスタライズ。[captions](../../crates/captions/src/lib.rs) は字幕ファイルの入出力、配置、映像への焼き込み。 |
| 音声処理 | [audio-dsp](../../crates/audio-dsp/src/lib.rs) は音量測定とエフェクト。[speech](../../crates/speech/src/lib.rs) は音声の文字起こし。[tts-text](../../crates/tts-text/src/lib.rs) は読み上げ前のテキスト正規化。[tts](../../crates/tts/src/lib.rs) は台本からの音声合成。 |
| テスト | [testkit](../../crates/testkit/src/lib.rs) はテスト用素材や比較に使う補助関数。[golden](../../crates/golden/tests/golden.rs) は描画結果を基準画像や別の描画経路と比較するテスト。 |

手元の版に合わせて対象を調べるには、リポジトリ直下で次を実行します。1行目は現在のコミットで管理するルートディレクトリ、2行目は各パッケージのマニフェスト、3行目はCargoが認識するパッケージやビルド対象を表示します。

```sh
git ls-tree -d --name-only HEAD
rg --files apps crates xtask -g Cargo.toml | sort
cargo metadata --locked --no-deps --format-version 1
```
