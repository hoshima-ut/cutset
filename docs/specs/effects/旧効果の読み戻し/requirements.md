# 旧効果の読み戻しの要件（FX-18）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

旧IDの効果と不足プラグインを識別し、移行結果・保持値・変換不能を示す。

## 受入条件

旧効果のパラメーター入り案件を開き、互換処理または不足能力が個別に示される。未対応時に保存し直しても保持可能な元データが失われない。

## 例外と復旧

プラグイン欠落時は未解決枠のまま保存できる。代替を取り消すと元データを復元でき、書き出し時にも影響箇所を知らせる。

## 参照資料と確認項目

- [A388](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/effects.html)　ボケ形状を選べるモダン効果を点光源に掛け、形状を変えた前後を同じフレームで比較する。（効果ライブラリは版混在。26.2・26.3・26.5追加分と27.0追加の8効果を区別）
- [A389](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/transitions.html)　動きの異なる二つのモダン切替を同じ編集点に適用し、途中の画と前後の尺を照合する。（版混在。3D Spinback／Slideは26.2、Shape Dissolveは26.3）
- [A390](https://helpx.adobe.com/premiere/desktop/add-video-effects/types-of-effects/animations.html)　透過ロゴにSpring Motionを置き、出入りの向きと弾む区間をフレーム送りで観察する。（公開手順）
- [A402](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-effects/manage-effects-and-plug-ins.html)　検証用の外部効果の有効・無効を切り替え、再起動後の一覧と依存案件の表示を比較する。（公開手順）
- [A429](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/effects-and-transitions-reorganization.html)　旧案件のディゾルブを開いた結果と新規の既定ディゾルブを比べ、旧版が自動置換されないか調べる。（公開手順）
- [A430](https://helpx.adobe.com/premiere/desktop/add-video-effects/effects-and-transitions-library/list-of-effects-and-transitions.html)　26系の変更一覧から旧名を一つ選び、新規追加可能・旧案件のみ描画・描画不能のどれかを照合する。（効果ライブラリは版混在。26.2・26.3・26.5追加分と27.0追加の8効果を区別）
- [A459](https://helpx.adobe.com/premiere/desktop/add-video-effects/commonly-used-effects/effects-and-transitions-removed-from-adobe-premiere.html)　削除済み効果を含む旧案件を開き、表示名・警告・描画を旧レンダーと比較する。（削除・Legacyの履歴。対象26.xで新規適用可能かと旧案件再生を別判定）
