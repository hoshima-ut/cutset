# prproj案件の読込の作業・試験（IO-57）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-57`、受入IDは `AC-IO-57`。着手は[UX-15](../../workflow/編集ソフト間の引き継ぎ/design.md#段階と出口)のH1判定の後。段階ごとに次の作業・受入・検査をグラフに登録する。packageは `filmcraft-interchange`、testは `it`。試験は `tests/it/prproj/` の下にモジュールを分け（1クレート1バイナリ）、`min_tests` は登録時点の通過件数にする。craft-libs側の試験は craft-libs の手順で回し、Cutset側では接続と照合の試験を回す。

| 作業ID | 先行 | 受入ID | 検査ID（絞り込み） |
| --- | --- | --- | --- |
| `PRPROJ-CONTAINER` | `HARNESS-CONTRACT` | `PRPROJ-REJECTS` | `PRPROJ-CONTAINER-TESTS`（`prproj::container::`） |
| `PRPROJ-HOSTILE` | `PRPROJ-CONTAINER` | `PRPROJ-REJECTS` | `PRPROJ-HOSTILE-TESTS`（`prproj::hostile::`） |
| `PRPROJ-SKELETON` | `PRPROJ-CONTAINER` | `PRPROJ-MATCHES-XML` | `PRPROJ-SKELETON-TESTS`（`prproj::skeleton::`） |
| `PRPROJ-DETAIL` | `PRPROJ-SKELETON` | `PRPROJ-MATCHES-XML` | `PRPROJ-DETAIL-TESTS`（`prproj::detail::`） |
| `PRPROJ-EFFECTS` | `PRPROJ-DETAIL` | `PRPROJ-MATCHES-XML` | `PRPROJ-EFFECTS-TESTS`（`prproj::effects::`） |

`AC-IO-57` には上の5つの検査をすべて登録する。試験は関係で書く（「見本Nの報告に要素キーXが含まれない」「許可表にない版は拒否する」）。件数や版の文字列そのものは確かめない。新しい版の見本で読込が失敗したら、その見本と失敗する試験を先に加えてから直す。

各作業の完了判定：

```sh
cargo fmt --check
cargo clippy -p filmcraft-interchange --all-targets -- -D warnings
cargo test --locked -p filmcraft-interchange --test it -- prproj::<段階>::
cargo xtask layers   # 依存を加えたとき
cargo xtask wasm     # interchange はL2
cargo xtask assets   # 見本を加えたとき
python3 tools/cutset_harness.py run PRPROJ-<段階>   # コミット済みのクリーンな作業ツリーで
```

- [ ] P1 容器と版：展開・上限・版判定・拒否理由、木構造の方針を記録する。
- [ ] P1 不正入力：下の表をすべて試験にする。
- [ ] P2 骨格：照合の基準で正解XMLと一致させる。
- [ ] P3 編集の詳細、P4 基本の調整：対象にした要素キーが全見本の取込報告に0件になる。
- [ ] 接続：`Format::Prproj`、`can_export`、`detect`、`EXTENSIONS`、新しい案件として開く命令、取込報告の要素キーと場所。画面・CLIで開き、原本不変、保存と再読込を確かめる。

## 具体的な試験

見本は基準案件A・B（[UX-15](../../workflow/編集ソフト間の引き継ぎ/tasks.md#具体的な試験)）から要素を一つずつ抜き出した部分集合として作る。素材はすべてCutsetの合成素材。

1. 1シーケンス・1クリップ（最小）
2. 映像2トラック・音声3トラック、空白とリンクした音声、4チャンネル素材のモノラル分割
3. 同じ素材の別配置、In/Outの異なる切り出し、開始タイムコード 01:00:00:00（29.97ドロップフレーム）
4. 速度50%・200%・逆再生・静止
5. クロスディゾルブ、ディップ（黒）、音声のフェード
6. シーケンスマーカーとクリップマーカー、ビンの入れ子、ラベル色
7. ネストしたシーケンスと複数シーケンス
8. 位置・スケール・回転・不透明度・音量・パンのキーフレーム
9. 素材を移動してオフラインにした案件、日本語（NFDを含む）と絵文字のファイル名・シーケンス名
10. 対象の2つの版で同じ内容を保存したもの

**見本の置き場所と来歴**。200 KB未満の見本は `crates/interchange/tests/fixtures/prproj/` に置き、大きいものはコーパス用リポジトリにコミットとsha256を固定して置く。各見本に `X.attribution`（作成者が公開に同意した表記・ライセンス・Premiereの版とビルド番号・OS・言語設定・作成日・sha256・同時に書き出したXMLのsha256・素材を生成したコマンド・作成票）を付け、`ATTRIBUTION.md` に行を加えて `cargo xtask assets` を通す。作成者は素材を共通のパス `/Users/Shared/cutset-handoff/` に置いて案件を作る。試験 `prproj::fixtures::no_personal_paths` で、見本とXMLにそのパス以外のホームディレクトリ・ホスト名・メールアドレスが現れないことを確かめる。

**不正入力**（`prproj::hostile::` に表でまとめる。すべて、パニックせずに `Err` を返すか報告付きで取り込み、途中の案件を作らない。壊れた入力はファイルとして置かず、試験の中で見本から作る）：

- 容器：0バイト、gzipでない平文XML、拡張子と中身の不一致、途中で切れたgzip、検査値の不一致、複数メンバー、展開爆弾、上限ちょうど（受理）と1バイト超え（拒否）、BOM付き・UTF-16
- 版：許可表にない版（見本の版の値だけを書き換えた派生）、想定外のルート要素
- 参照：存在しない素材ID、IDの重複、ネストの循環、自分自身を含むシーケンス、深さ `MAX_NESTING_DEPTH` ちょうどと1超え
- 骨格：クリップ0のシーケンス、トラック0、長さ0と1フレームのクリップ、先頭と末尾のクリップ、音声だけのシーケンス、5.1チャンネルとモノラル
- 値：速度0・負・極端な値、クリップ範囲外のキーフレーム
- パス：Windows形式、NFDの日本語、絵文字、非常に長い名前
- 未対応の種類：調整レイヤー、マルチカメラ、グラフィックのクリップ（要素キーと場所が報告に出る）
- 原本：読込の前後でsha256と更新日時が変わらず、書きかけのファイルが残らない

`proptest`（既存の開発用依存）で、切断・ビット反転・巨大展開・深い入れ子を加える。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 正解XMLの読込：[crates/interchange/tests/it/fcp7.rs](../../../../crates/interchange/tests/it/fcp7.rs)（公開APIを通るので、共有ライブラリの本番経路を確かめる）。
- 壊れた入力の前例：[crates/interchange/tests/it/aaf_omf.rs](../../../../crates/interchange/tests/it/aaf_omf.rs)、ネストの循環：[crates/interchange/tests/it/cyclic_subclips.rs](../../../../crates/interchange/tests/it/cyclic_subclips.rs)。
