# ジャンプカットの補間の要件（FX-17）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

人物映像の不連続な境目を解析し、補間候補を元のカットと比較する。

## 受入条件

固定カメラの正面顔とカメラ移動・複数人で比較し、不自然な際に通常のカットへ戻せる。

## 例外と復旧

顔を特定できない、または複数候補がある場合は判定不能として元のカットを維持する。再生成中に素材が変わったら旧結果を適用しない。

## 参照資料と確認項目

- [A476](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/morph-cut-overview.html)　同じ人の二発言をモーフでつなぎ、口と顔の形が滑らかにつながる区間と破綻する区間を比べる。（公開手順）
- [A477](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/apply-morph-cut-to-smoothen-jump-cuts.html)　固定カメラのジャンプカットへMorph Cutを置き、解析完了後の中間像を原カットと見比べる。（公開手順）
- [A478](https://helpx.adobe.com/premiere/desktop/add-video-effects/apply-video-transitions/morph-cut-transition-options.html)　モーフカットの長さや編集点との位置を変え、再解析後に口の形が破綻しにくい範囲を見る。（公開手順）
