# FilmCraftの更新を取り込む

このforkの `origin` は `hoshima-ut/cutset`、`upstream` は `storytold/filmcraft` です。新しいクローンで `git remote -v` にupstreamがなければ `git remote add upstream https://github.com/storytold/filmcraft.git` を一度実行します。

| 文書 | 上流の更新時の扱い |
| --- | --- |
| [Cutsetの製品仕様](../specs/index.md)、[操作マニュアル](../manual/README.md)、[開発計画](roadmap.md) | Cutsetで編集する文書。上流の変更を採用して動作が変わる場合に更新します。 |
| [FilmCraft技術資料](../reference/filmcraft/README.md) | 分岐元の資料を保管します。参照先を移すときは本文の改稿を別の変更にすると、Gitが移動を検出しやすくなります。 |
| [FilmCraftのロードマップ](../reference/filmcraft/upstream-roadmap.md) | 上流ルートの `ROADMAP.md` に対応します。分野別の開発予定はCutsetのロードマップに書きます。 |

## 最初に競合を調べる

```sh
git fetch origin main
git fetch upstream main
git rev-list --left-right --count origin/main...upstream/main
git merge-tree --write-tree --name-only origin/main upstream/main
```

最後のコマンドはGit 2.38以降で使えます。作業中のファイルやブランチを変更せずにマージ結果を計算し、終了コード0は自動統合可能、1は競合、その他はコマンドエラーです。取り込みを決めたら、検査した両端のコミットを固定して別の作業コピーで検証します。[Gitの公式マニュアル](https://git-scm.com/docs/git-merge-tree)

```sh
cutset_rev=$(git rev-parse origin/main)
filmcraft_rev=$(git rev-parse upstream/main)
git worktree add -b codex/upstream-sync ../cutset-upstream-sync "$cutset_rev"
cd ../cutset-upstream-sync
git merge --no-commit --no-ff "$filmcraft_rev"
git status --short
```

競合した資料は、分岐点・上流・Cutsetの差分を照合します。仕様、ブランド、署名設定、更新先、GitHub Actions設定に影響する変更は個別に確認します。既存の検証と、更新された機能のローカルテストを実行し、マージ結果をレビューしてから採用します。試験中のマージを取りやめるときは、この専用コピーで `git merge --abort` を実行します。

## 2026-11-26の検証

分岐点 `8fe98718`、Cutset `40511535`、FilmCraft `a7dcaa22` を比較しました。上流側の8コミットに対し、元の構成では上流ルートの `ROADMAP.md` が変更と削除の競合になりました。上流用のロードマップを参照資料として配置した後は、同じ上流版の更新が移動先へ自動で適用されました。上流のロードマップ本文がリンク先の調整を除いて一致し、Cutsetのロードマップの内容も維持されました。この検査はソースを取り込む前の確認です。
