# 作業色空間の要件（CO-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

シーケンスの作業空間、トーンマッピングと変換順序を明示する。

## 受入条件

LogからSDR・HDRを作り、ガンマの二重適用、白飛び、域外色のつぶれをスコープで確認する。

## 例外と復旧

作業空間で評価できない効果は対象の配置と処理精度を示す。素材個別の上書きや納品設定を暗黙に書き換えない。

## 参照資料と確認項目

- [A029](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/color-preferences.html)　モニターの色設定を変え、ファイルへ書き出される色タグとの違いを確認する。（公開手順）
- [A574](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/color-settings.html)　案件の色設定を保存し直し、再び開いたときに作業色空間を確認する。（公開手順）
- [A591](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/about-color-management.html)　入力・作業・出力の各空間を表示し、Log素材の自動認識結果を記録する。（公開手順）
- [A592](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/how-color-management-works.html)　既知の入力色から作業空間を経て出力変換する順序を基準チャートで照合する。（公開手順）
- [A593](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/lumetri-enhancements.html)　Lumetriの同じ数値を異なる色管理設定で適用し、意図した変換順を識別する。（公開手順）
- [A594](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/color-management-options.html)　トーンマップや作業色空間の選択肢を変え、出力ハイライトへの影響を確認する。（公開手順）
- [A596](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/configuring-sequence-color-management.html)　シーケンスごとに色空間を変更し、他のシーケンスに波及しない。（公開手順）
- [A598](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/customize-color-setup-presets-for-new-or-existing-sequences.html)　カラープリセットを新規・既存シーケンスに適用し、既存編集点を保持する。（公開手順）
- [A600](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/disabling-color-management.html)　自動管理を外したとき、明示したLUTと未変換素材を識別できる。（公開手順）
- [A602](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/tone-mapping-in-premiere.html)　HDRハイライトをSDRへ収め、白飛びと彩度の変化をスコープで測る。（公開手順）
