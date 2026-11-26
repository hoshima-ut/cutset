# 補正の重ね順の要件（CO-10）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

複数の補正を命名・並べ替え・バイパスし、ショット間の転用を管理する。

## 受入条件

一次補正・部分補正・ルックを独立に切り替え、保存後も順序とマスクが維持される。

## 例外と復旧

コピー先に必要なLUTがない時は欠けた段だけを示す。並べ替え中のキャンセルで元の順序を復元する。

## 参照資料と確認項目

- [A575](https://helpx.adobe.com/premiere/desktop/correct-color/color-correction-fundamentals/create-and-edit-multiple-lumetri-color-effects.html)　Lumetriを二段積み、一方の無効化と順序変更の違いを同じフレームで比べる。（公開手順）
- [A620](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/managing-multiple-color-operations.html)　複数の調整を並べ替え、一つだけ無効にしたときの結果が再現する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A621](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/applying-clip-operations.html)　一配置だけにグレードを適用し、隣の同素材ショットが変化しない。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A622](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/applying-operations-to-the-sequence.html)　シーケンス全体のグレードの上に個別調整がある案件で作用順を確かめる。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A623](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/using-custom-groups.html)　グループのメンバーを外し、再調整時に外したショットへ波及しない。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A624](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/copy-and-paste-for-grade-management.html)　グレードの一部を別クリップにコピーし、貼らなかった項目の値を保つ。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A626](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/lumetri-color.html)　旧Lumetri案件を比較版で開き、元の調整値と出力の変化を記録する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
