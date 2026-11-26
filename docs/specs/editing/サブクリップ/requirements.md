# サブクリップの要件（ED-17）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

原本に対する範囲参照を作り、トリム可能な余白を制限または解放する。

## 受入条件

一つのインタビューから二つの発言の項目を作り、片方だけ範囲を直す。

## 例外と復旧

原本を再リンクした結果が短い場合は不足範囲を警告し、他のサブクリップの参照点を繰り上げない。

## 参照資料と確認項目

- [A204](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/create-a-subclip-from-the-project-panel.html)　Projectパネルから元素材の前半と後半を別のサブクリップとして登録し、双方の利用可能区間を比較する。（公開手順）
- [A205](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/create-a-subclip-from-the-timeline.html)　既にトリム済みのタイムライン配置からサブクリップを作り、元テイクの該当区間がビンへ登録されるか見る。（公開手順）
- [A206](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/convert-subclip-to-master-clip.html)　サブクリップをソースクリップへ変換し、従来の範囲外のフレームにアクセスできるか確かめる。（公開手順）
- [A207](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/adjust-media-start-and-end-times-of-subclip.html)　サブクリップの開始・終了許容範囲を調整し、新たに使える範囲と元ファイルの長さを別々に照合する。（公開手順）
