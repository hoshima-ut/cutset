# Cutset

![Cutsetのロゴ](assets/app-icon/hicolor/128x128/apps/ai.storyteller.filmcraft.png)

Cutsetは、FilmCraftをベースにしたオープンソースの動画編集ソフトです。AIによる編集支援と、他の動画編集ソフトとの編集データの受け渡しに取り組んでいます。

## インストールと使い方

Macへの導入、素材の読み込み、カット、字幕、書き出しの手順をまとめています。配布担当者は署名と公証を済ませたDMGを作成できます。[Macへのインストール](docs/manual/install.md) ・ [操作マニュアル](docs/manual/README.md) ・ [配布用DMGの作成](docs/development/build-installer.md)

## 仕様と開発計画

既存機能と追加機能の動作、検証条件、実装の順序を公開しています。[ドキュメント](docs/README.md) ・ [機能別の仕様](docs/specs/index.md) ・ [マイルストーン](docs/development/milestones.md) ・ [AIモデルと個人プランの設計](docs/architecture/model-connections.md)

## 変更を始める前に

Git・Python 3.9以上・Gitleaks 8.30.1を用意し、クローンごとにリポジトリ直下で `tools/install-hooks` を一度実行します。`python3 tools/check_handbook.py` で文書の入口、`tools/secret-guard staged` でコミット予定の内容を確認できます。[秘密情報の保護と復旧](docs/security/credentials.md)

## 手元で起動する

macOSではXcode Command Line ToolsとRust stable 1.95以上を用意し、リポジトリのルートで次を実行します。現在のCargoパッケージ名と生成バイナリ名は上流と同じです。他のOSの前提と、ビルド時に追加できる日本語フォントは上流の手引きにあります。[開発環境](docs/development/rust.md)

```sh
cargo test --locked -p filmcraft-time
cargo build --locked --release -p filmcraft -p filmcraft-cli
mkdir -p target/first-run
./target/release/filmcraft --demo --data-dir "$PWD/target/first-run/profile"
```

## 開発に参加する

- ソースを初めて読む方は、[ディレクトリ案内](docs/development/repository-map.md)で構成を確認し、[Rustコードの読み方](docs/development/reading-rust.md)でマーカーの追加と取り消しを追えます。
- Cutsetの目的・設計・作業順は[開発ハンドブック](docs/development/README.md)で確認できます。AIエージェントによる変更は[エージェント向けの入口](AGENTS.md)から始めます。
- 編集エンジンの構造、ローカルテスト、既存の編集命令はFilmCraftの技術資料を参照します。[構成](docs/architecture/engine.md) · [テスト](docs/verification/engine.md) · [CLI・MCP](docs/reference/filmcraft/agents.md)
- FilmCraft v0.20.1の機能一覧と対応環境は、上流のREADMEで確認できます。[上流の機能一覧](https://github.com/storytold/filmcraft/blob/v0.20.1/README.md)

## ライセンスとクレジット

Cutsetのロゴと配布用の画像はこちらで確認できます。[ロゴの設計と候補](docs/development/visual-identity.md)

FilmCraft本体はMITまたはApache-2.0を選択して利用できます。著作権表示は「Copyright (c) 2026 ArtCraft Team and the FilmCraft contributors」です。フォント、画像などの素材には個別の条件があり、ArtCraftの名称・ロゴにはブランド利用条件が適用されます。[MIT](LICENSE-MIT) · [Apache-2.0](LICENSE-APACHE) · [NOTICE](NOTICE) · [素材の帰属表示](ATTRIBUTION.md) · [ブランド利用条件](docs/brand/LICENSE-brand.txt)
