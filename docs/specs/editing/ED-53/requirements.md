# ED-53 複数ターゲットの優先順位 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

貼り付け、フレーム照合、行移動の対象トラックを操作ごとに決定する。

## 受入条件

V1とV4に別のカメラ映像を重ねて挿入先と開いた素材を照合。非対象トラックだけにある境界で停止しないかも確かめる。

## 例外と復旧

最優先行の位置が空なら、有効な次候補に移る操作と空のまま扱う操作を区別し、実際の行を示す。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/work-with-clips-on-the-timeline-using-track-targeting.html)
