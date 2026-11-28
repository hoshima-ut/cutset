# Cutset 開発ハンドブック

Cutsetの開発手順、設計上の判断、検証方法をまとめています。

| 必要なこと | 読む文書 |
| --- | --- |
| 社内向けの配布物を作る | [ソースからビルド](build-installer.md) ・ [利用者の操作マニュアル](../manual/README.md) |
| FilmCraftの更新を取り込む | [上流との差分と競合を確認する](upstream-sync.md) |
| ソースを読む順番を決める、Rustの型と編集履歴の関係を理解する | [ディレクトリ案内](repository-map.md) ・ [Rustコードの読み方](reading-rust.md) |
| 編集者に何を届けるか、編集命令・互換性・Webの境界を決める | [製品設計](../architecture/product.md) |
| 画面と操作を速く、編集者に寄り添ったものにする | [最速で編集できる画面の設計](../architecture/editor-ux.md) ・ [デザインのDNA](visual-identity.md#デザインのdna) |
| 次の作業を一つ選ぶ、担当を交代する | [作業台と再開メモ](progress.md) |
| AIと人の分担、変更の粒度と検証方法を決める | [開発規約](engineering.md) |
| 追跡対象とpush履歴を検査してから作業する | [鍵を公開しない開発手順](../security/credentials.md) |
| 基準案件を動かして編集結果を比較する | [素材の準備と編集者用評価票](../verification/interview.md) |

## 最初の15分

1. Git、Python 3、Gitleaksを用意し、リポジトリ直下で `tools/install-hooks` を実行する。作業コピーを新設したときも行う。
2. `python3 tools/check_handbook.py` と `tools/secret-guard staged` を実行する。Rustの開発環境を準備したら `cargo test --locked -p filmcraft-time` で時間型を扱うパッケージのビルドを確認する。編集の振る舞いは[Rust読解ガイドの履歴テスト](reading-rust.md)で試せる。初回のビルドは環境によって時間がかかる。
3. 作業台01の受入条件を読み、既存の無音検出と文字起こしパネルから対象コードをたどる。編集者の試聴が必要なケースには担当を付ける。再開時は同じ作業台を更新する。

## 文書の置き場所

機能別の要件・設計・作業は[仕様索引](../specs/index.md)、実装判断は[アーキテクチャ](../architecture/product.md)、試験は[検証資料](../verification/coverage.md)に置きます。[文書一覧](../README.md)から用途別に探せます。

READMEは利用者の入口、AGENTS.mdは開発エージェントの入口、SECURITY.mdは報告窓口。社内案件の素材・未公開仕様・利用者別の評価記録は管理者が許可した私有の保管先を使う。公開する再現手順には合成素材と必要最小限の結果を書く。
