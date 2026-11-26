# 作業面を跨ぐ位置の維持の要件（UX-14）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

色・音・編集・納品へ移動しても同じ発言と再生位置へ戻れるようにする。

## 受入条件

色を変えて編集に戻っても、現在の発言と前後を失わない。

## 例外と復旧

作業中の編集で発言の配置が消えた場合は参照喪失を表示し、同じ時刻に入った別配置を元の発言として表示しない。

## 参照資料と確認項目

- [A603](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/color-mode-basics.html)　比較版でColor Modeへの入口を確認し、26系正式機能とは別欄に記録する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A604](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/using-color-mode-with-color-management.html)　色管理を有効にしたシーケンスでColor Modeに移り、作業・出力空間の値を照合する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A605](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/work-in-color-mode.html)　編集画面とグレーディング画面を往復し、再生中のショットを維持する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A606](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/open-a-sequence-in-color-mode.html)　二つのシーケンスから対象を指定し、別シーケンスに誤って調整しない。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A607](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/color-mode-workflow.html)　一連のショット選択、調整、比較、戻しを一回通し、確定した変更を確認する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A608](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/working-with-the-clip-grid.html)　クリップグリッドで選択を移し、モニターと調整対象のショットが一致する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A609](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/understanding-heads-up-displays.html)　HUDを出した状態で映像上の値を変更し、閉じても適用結果を保持する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A610](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/default-adjust-operation.html)　初期のAdjust操作を一項目だけ変え、リセット後に元画像へ戻る。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A611](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/color-adjustment-in-edit-mode.html)　Edit側で作った調整をColor側で確認し、重複する変更を作らない。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A612](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/about-the-clip-grid.html)　グリッド上の表示順とシーケンス順を比べ、同一素材の別配置を識別する。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A613](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/color-tools-panel-overview.html)　カラー用ツールの選択を切り替え、選択対象・調整値・作用範囲が読める。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
- [A614](https://helpx.adobe.com/premiere/desktop/correct-color/color-mode-fundamentals/color-monitor-overview.html)　カラーモニターで同一のフレームを保持しながらグレード前後を見比べる。（Color Modeは26.2時点でベータ、27.0で正式。26系正式仕様から分離）
