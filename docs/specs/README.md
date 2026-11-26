# Cutset 製品仕様

各機能の要件、設計、検証作業を分野別に管理します。[機能索引](index.md)から対象の機能IDを選んでください。

| 探したいもの | 入口 |
| --- | --- |
| 各機能の振る舞い、現状、受け入れ条件 | [機能索引](index.md) ・ [機械可読台帳](data/catalog.json) |
| 実装済みの編集命令と入口 | [上流コマンド台帳](data/native-commands.tsv) ・ [エンジンの命令定義](../../crates/engine/src/commands.rs) |
| 公開資料を元に確認する操作 | [公開資料と個別確認ケース](data/sources.json) |
| プラグイン、APIキー、個人プラン | [AIモデルの接続と編集権限](../architecture/model-connections.md) |
| 実装の順序と完了判定 | [マイルストーン](../development/milestones.md) ・ [仕様グラフと検証ループ](../development/harness.md) |
| 最初の編集を試す | [インタビュー案件](../verification/interview.md) ・ [進行中の作業](../development/progress.md) |

## UI・UX・AXを各仕様で確かめる

| 観点 | 例「選んだ間を詰める」の受入 |
| --- | --- |
| UI（画面と操作） | フォーカス、選択範囲、試聴中、保留・採用、確定前後を識別する。キー操作と読み上げで同じ判断ができ、日本語入力中に編集キーが発火しない。 |
| UX（仕事を終える体験） | 編集者が呼吸を残し、ロックされたBGMを維持し、失敗しても元の案件へ戻れる。基準案件で完了時間、操作数、意図しない変更、手修正の理由を記録する。 |
| AX（ここではAI・エージェントの操作体験） | 能力・対象ID・時間単位・予想される変更・失敗理由を機械が読める。GUIと同じ編集契約を通り、同意範囲、競合、再送、Undoの結果を再現できる。 |
| アクセシビリティ | 入力方式、視覚、聴覚の違いに対応する。フォーカスの復帰、名前と状態の読み上げ、色以外の識別、試聴範囲の可視化を確かめ、実機・支援技術・未検証条件を記録する。 |

## 編集グラフと仕様グラフ

編集側では既存の案件、シーケンス、素材、配置、トラック、字幕をIDで扱う。素材を参照する辺、映像と音声を同期する辺、ネスト、時間変換をたどり、操作が動かす範囲を求める。同じ素材の別配置、ロックしたトラック、選択外の字幕も確認する。基準版に対する候補には切断・短縮する区間と残す関係を記録し、確定直前に検証する。UndoでフレームとIDの関係が戻ることを比較する。[編集モデル](../../crates/project) ・ [最初の編集取引](../architecture/product.md)

開発側では機能、作業、受入条件、チェック、コミットに紐づく結果をグラフ化する。変更した仕様から影響範囲を検索できる。機械で通せる条件をローカルで反復し、音の自然さ、フォーカスの分かりやすさ、実サービスの資格は担当者の観測を記録する。[実行方法](../development/harness.md)

## 公開仕様の読み方

比較対象はPremiere 26.xとFilmCraftの公開資料・ソース。安定版、ベータや別版、外部サービス、実機が必要な確認を区別する。Cutsetの仕様は編集者が達成する操作・結果を自分たちの言葉で定める。公開資料の照合件数は操作の実装数やPremiereとの完全一致を表さない。26.xの修正はAdobeの版別リリースノートに戻って照合する。[Adobe Premiereリリースノート](https://helpx.adobe.com/premiere/desktop/whats-new/release-notes.html)

### 継承コマンドの読み方

コマンド台帳はCLIの `commands --json` が返す命令を1行ずつ収録し、操作の表示名、引数、メニュー、既定キー、主に関係する仕様IDとエンジンの参照先を付ける。名前空間やメニューに現れない入口も含む。既存命令の維持条件は、同じID・引数・前提で呼べること。選択なし・ロック・対象欠落ではその命令の可否やエラーを確認し、編集命令は操作前後の案件を比較する。各行の存在確認に使うコマンドは `filmcraft-cli commands --json`、個別の引数とその時点の有効状態は `filmcraft-cli describe <id>` で確認できる。メニュー表示や全引数を個別に実行した記録とは区別する。

台帳の基準は本forkの分岐時点 `8fe98718`。v0.20.1 の一覧に加えて、その後の上流で追加された読取命令 `timeline.slipPreview` を含む。ビルドしたCLIで以下を実行すると、台帳からの欠落・余分な命令・重複と、表示名・メニュー・既定キー・引数のずれを検査できる。

```sh
mkdir -p target
./target/release/filmcraft-cli commands --json > target/cutset-commands.json
python3 tools/check_catalog_links.py --commands-json target/cutset-commands.json
```


## 仕様を更新する

各機能の `requirements.md` が目的・受入条件・例外の正本です。`design.md` に操作、状態の変化、処理の入出力、使える実装を記載します。`tasks.md` には具体的な試験と残る作業を記録します。試験を通した場合は対象の版、入力と結果を残してください。

要件を変更したら `python3 tools/check_catalog_links.py --write-overview` で目的・受入条件を機械台帳に反映し、分野別索引を更新します。目標マイルストーン・実装方針・参照先は `data/catalog.json` で管理します。設計書と作業表は直接編集できます。新しい機能を加えるときは同じ分野に3文書を作り、台帳と対象IDの管理範囲を更新してください。

```sh
python3 tools/check_handbook.py
python3 tools/cutset_harness.py validate
```

[分野別の操作条件](shared/interaction.md) ・ [レンダリングと形式別の条件](shared/rendering.md) ・ [横断試験](data/journeys.json) ・ [検証範囲](../verification/coverage.md)
