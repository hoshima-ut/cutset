# 仕様から検証結果をたどる

[機能カタログ](../specs/data/catalog.json)の各IDを起点に、対象機能、実装作業、受入条件、検証コマンド、手元の観測結果を結ぶ。たとえば `AI-03` は編集候補のプレビュー全体、`CHECK-PREVIEW` はそのうち試用素材A、B、CのフレームをCLIで確認する作業を表す。

```sh
python3 tools/cutset_harness.py validate
python3 tools/cutset_harness.py show AI-03
python3 tools/cutset_harness.py impact AI-03
python3 tools/cutset_harness.py ready
python3 tools/cutset_harness.py loop --limit 2
python3 tools/cutset_harness.py graph
```

| 関係 | 意味 |
| --- | --- |
| feature → task | この仕様に関係する実装作業。作業ごとに対象とする範囲を明記する。 |
| task → task | 先行作業の機械検証が通ると次の作業を実行できる。 |
| task → acceptance | 作業の受入条件。機能ごとの全文は各機能の `requirements.md` に記す。 |
| acceptance → check | この条件についてコマンドで測定できる部分。 |
| check → evidence | この作業、コミット、作業ツリーに対してテストが通った記録。 |

`show` は入出力の直接の関係を、`impact` は指定ノードから関係を順にたどって到達する作業・条件・検証を返す。`graph` はノードと種類付きの有向辺をJSONで出力する。型を指定するときは `task:CHECK-PREVIEW` のように書く。

## 新しい機能を作業へ落とす

1. 各機能の `requirements.md` に編集者の操作と観測可能な受入条件を記す。`python3 tools/check_catalog_links.py --write-overview` で台帳と索引を同期する。ハーネスは台帳から `BUILD-機能ID` の作業と `AC-機能ID` の受入条件を生成する。検証が未登録の機能は `planned` と表示される。
2. 小さく実装できる範囲を[グラフ定義](../specs/data/graph.json)に追加する。`specs` で機能、`requires` で先行作業、`acceptance` でその範囲の判定を指定する。受入条件は `checks` で検証IDに接続する。機能全体を検証できるようになったら `AC-機能ID` に検証IDを登録する。全体の受入文はカタログから読み込まれる。
3. テストを追加し、編集途中はテストスクリプトを直接実行する。カタログやグラフに加えて、実装とテストもコミットし、ローカルの `loop` を実行する。検証コマンドを追加する際はランナー側の許可リストと回帰テストも更新する。
4. `review_pending` の作業は、独立したレビュー担当が結果を照合する。音を聞く、UIで操作するなどの未検証部分は引継ぎに記す。編集者による採否と公開判断は[開発手順](engineering.md)に沿って記録する。

## 検証の再現

`run CHECK-PREVIEW` は指定した作業を再実行する。`loop --limit N` は検証可能な先頭の作業を一件ずつ実行する。上限は1回から10回。最初の失敗で終了コード1、次の実行で失敗した作業を再検証する。定義不備や前提未充足は終了コード2。通常の出力には検証ID、引数、終了コード、通ったテスト数を含め、診断が必要な場合は表示されたコマンドを直接実行する。

証跡は追跡対象外の `target/cutset-harness/<コミットSHA>/<作業ID>.json` に保存する。開始時と終了時にクリーンなコミットを照合し、利用時にコミット、ツリー、仕様定義のハッシュ、検証ID、各テスト結果を確認する。ブランチが更新されたときは対象コミットで再実行する。証跡はローカル上で編集可能な開発記録であり、第三者による署名や製品の受入承認を表すものではない。

同じコミットで実行中のランナーがあると二重実行を停止する。強制終了後にロックだけが残った場合は、該当コミットのランナーが停止したことを確認してから証跡フォルダーの空ディレクトリ `.running` を取り除く。
