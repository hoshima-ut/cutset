# 挿入先と操作先の要件（ED-12）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材からの流入先と既存配置に対する編集先を別々に指定する。

## 受入条件

V1素材をV2に挿入。別のV1をターゲットにしたMatch Frameは再生ヘッド下のV1素材を開く。

## 例外と復旧

パッチ先がロック済み、または種類が不一致なら挿入を止め、他の空き行を暗黙で選択しない。

## 参照資料と確認項目

- [A208](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/add-media-to-the-timeline-using-source-patching.html)　V1の入力をV2にパッチし音の入力を外して挿入したときに、V2へ映像のみが入るか確認する。（公開手順）
- [A209](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/work-with-clips-on-the-timeline-using-track-targeting.html)　V1とV4が対象のときの貼り付け先とMatch Frameで開く素材を照合し、コマンド別の選択優先順位を確かめる。（公開手順）
