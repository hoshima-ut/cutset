# 映像スコープの要件（CO-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

波形、RGBパレード、ベクトルスコープ、ヒストグラムを組み合わせる。

## 受入条件

グラデーション、カラーバー、HDRハイライトで、選んだ信号と目盛の関係を確認する。

## 例外と復旧

入力がオフラインなら前フレームの数値を現時刻の測定値として表示しない。近似・間引き測定を用いる場合は条件を表示する。

## 参照資料と確認項目

- [A588](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/available-lumetri-scopes.html)　波形・パレード・ベクトルスコープを切り替え、同じパッチの輝度と色相を読む。（公開手順）
- [A590](https://helpx.adobe.com/premiere/desktop/correct-color/add-color-effects/display-lumetri-scopes.html)　複数スコープの同時表示と閉じて開き直したときの表示設定を確かめる。（公開手順）
- [A616](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/working-with-video-scopes.html)　カラー作業中のスコープで補正結果が再生・停止の両方で更新される。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
