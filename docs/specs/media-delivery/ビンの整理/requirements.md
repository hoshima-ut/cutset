# ビンの整理の要件（IO-15）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

ビン、任意配置、列、サムネイルと使用箇所から原本・配置を探索する。

## 受入条件

同じ名前の子ビンを別作品の下に置き、並べ替え後も所属先と配置済みクリップを維持。

## 例外と復旧

自分自身または子孫へのビン移動は拒否する。同名の別ビンは所属階層を併記する。

## 参照資料と確認項目

- [A137](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/bins-overview.html)　ビンの階層を作り、ディスク上のフォルダーを変えずに同一案件内で採用素材を整理できるか試す。（公開手順）
- [A138](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/add-and-delete-bins.html)　空ビンと素材を含むビンを用意して削除操作を行い、案件内の項目とディスク原本の扱いを確認する。（公開手順）
- [A139](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/open-and-close-bins.html)　親ビンと子ビンを別々に開き、子だけ閉じた後も親の一覧と素材参照が保持されるか試す。（公開手順）
- [A140](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/manage-bins.html)　複数の項目を別のビンへまとめて移し、既に配置したクリップが同じ素材を指すか再生して確認する。（公開手順）
- [A141](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/change-bin-behaviors.html)　ビンを開く動作の設定を変えて、同じ操作からタブ・既存パネル・別ウィンドウのどこが開くか記録する。（公開手順）
- [A142](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/organize-bins.html)　素材名順と撮影順でビンを並べ替え、同じ選択項目を見失わずに各表示で見つけられるか試す。（公開手順）
