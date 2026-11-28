# prproj案件の書き出しの作業・試験（IO-58）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-58`、受入IDは `AC-IO-58`。H6の判断まで検査を付けない。

- [ ] 着手条件の判定と、対象の版・要素を記録する。
- [ ] 着手する場合、IO-57の木構造で `write(parse(x)) == x` を全見本で確かめる。

## 具体的な試験

基準案件A・BをCutsetから書き出し、対象版のPremiereで開く。要素キーごとの判定をXML経路の結果と比べる。Premiereで保存し直したファイルをCutsetで読み戻し、元の案件と照合の基準で一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- 書き出しの既存試験：[crates/interchange/tests/it/api.rs](../../../../crates/interchange/tests/it/api.rs)。
