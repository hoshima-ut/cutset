# Cutset

Cutsetは、ArtCraftチームとFilmCraftのコントリビューターが開発した動画エディタFilmCraftを土台にしたOSSプロジェクトです。編集者がAIの提案を原音と聴き比べ、残したい一呼吸を自分で選び、その編集を別のツールへ引き継げることを目指しています。[開発ハンドブック](handbook/README.md)

最初の試作は、64秒の日本語インタビューを60秒に仕上げる作業です。上流版の手編集を基準に、候補を一つずつ試聴して採用し、一度のUndoで戻せる操作を設計します。固定事例の試聴範囲を計算する開発用CLIがあります。画面での候補試聴とAIモデル接続は計画段階です。[パイロットの素材と評価手順](handbook/pilot.md)

## 何が使え、何を作るか

既存機能と追加機能の動作、検証条件、実装の順序を公開しています。[製品仕様](spec/README.md) ・ [マイルストーン](spec/milestones.md) ・ [AIモデルと個人プランの設計](spec/model-connections.md)

## 変更を始める前に

Git・Python 3.9以上・Gitleaks 8.30.1を用意し、クローンごとにリポジトリ直下で `tools/install-hooks` を一度実行します。`python3 tools/check_handbook.py` で文書の入口、`tools/secret-guard staged` でコミット予定の内容を確認できます。[秘密情報の保護と復旧](handbook/secrets.md)

## 手元で起動する

macOSではXcode Command Line ToolsとRust stable 1.95以上を用意し、リポジトリのルートで次を実行します。現在のCargoパッケージ名と生成バイナリ名は上流と同じです。他のOSの前提と、ビルド時に追加できる日本語フォントは上流の手引きにあります。[開発環境](docs/contributing.md)

```sh
cargo test --locked -p filmcraft-time
cargo build --locked --release -p filmcraft -p filmcraft-cli
mkdir -p target/first-run
./target/release/filmcraft --demo --data-dir "$PWD/target/first-run/profile"
```

## 開発に参加する

- Cutsetの目的・設計・作業順は[開発ハンドブック](handbook/README.md)で確認できます。AIエージェントによる変更は[エージェント向けの入口](AGENTS.md)から始めます。
- 編集エンジンの構造、ローカルテスト、既存の編集命令はFilmCraftの技術資料を参照します。[構成](docs/architecture.md) · [テスト](docs/testing.md) · [CLI・MCP](docs/agents.md)
- この試作の基準はFilmCraft v0.20.1です。編集・音声・カラー・書き出しの機能一覧と対応環境は、基準版のREADMEで確認できます。[上流の機能一覧](https://github.com/storytold/filmcraft/blob/v0.20.1/README.md)

## ライセンスとクレジット

FilmCraft本体はMITまたはApache-2.0を選択して利用できます。著作権表示は「Copyright (c) 2026 ArtCraft Team and the FilmCraft contributors」です。フォント、画像などの素材には個別の条件があり、ArtCraftの名称・ロゴにはブランド利用条件が適用されます。[MIT](LICENSE-MIT) · [Apache-2.0](LICENSE-APACHE) · [NOTICE](NOTICE) · [素材の帰属表示](ATTRIBUTION.md) · [ブランド利用条件](docs/brand/LICENSE-brand.txt)
