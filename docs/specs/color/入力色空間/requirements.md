# 入力色空間の要件（CO-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

既知のRAW・Log・色空間を識別し、素材単位で解釈と入力変換を選ぶ。

## 受入条件

同一のグレーカードを異なるカメラで撮った素材と、タグが誤った素材の両方を確認する。

## 例外と復旧

タグ欠落やメタデータの矛盾は「未確定」と表示する。利用できないカメラ変換を指定した際は、利用できる解釈を選び直せる。

## 参照資料と確認項目

- [A595](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/manage-source-media-colors-in-program-monitor.html)　同じ素材を素材モニターと完成モニターで開き、表示条件による差を説明できる。（公開手順）
- [A597](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/color-management-using-clip-modify.html)　誤認識された素材に入力色空間を手動指定し、その素材を共有する各配置で確認する。（公開手順）
- [A788](https://helpx.adobe.com/premiere/desktop/troubleshooting/playback-issues/premiere-exports-look-washed-out.html)　薄く見える出力を別再生器とスコープで比較し、タグ・変換・表示器のどこで差が出たか示す。（障害診断）
