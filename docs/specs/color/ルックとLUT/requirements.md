# ルックとLUTの要件（CO-05）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

外部LUTまたは作成済みのルックを適用し強度と色空間を指定する。

## 受入条件

入力変換と創作Lookの適用順を固定し、別端末でLUT参照が切れたときに判別できる。

## 例外と復旧

同名でも内容が異なるLUTは差し替え候補として表示する。欠落時は再リンクか明示バイパスを選べる。

## 参照資料と確認項目

- [A581](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/install-custom-look-up-table-files.html)　ユーザー追加LUTを配置し、再起動後に読み込み可否と表示名を確認する。（公開手順）
- [A582](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/add-look-up-tables.html)　入力用と演出用LUTを切り替え、適用順と同時適用の結果を比較する。（公開手順）
- [A583](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/save-or-export-look-up-tables.html)　書き出したLUTを別案件に読み、対応する変換だけをチャートで再現できる。（公開手順）
- [A589](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/apply-lumetri-looks.html)　クリエイティブルックを適用し、強度の両端とバイパスの表示を比較する。（公開手順）
- [A617](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/grading-clips-using-adjust.html)　Adjustで露出を変え、他の操作を無効にした状態で結果を比較する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A618](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/grading-clips-using-style.html)　Styleの適用量を変更し、元の補正値とスタイルによる変化を区別する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A619](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/available-style-modules.html)　スタイルの各モジュールを単独で有効にし、対象とする色や質感を確認する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
