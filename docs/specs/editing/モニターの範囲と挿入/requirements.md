# モニターの範囲と挿入の要件（ED-52）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材側の範囲・映像のみ・音のみの指定と、完成側の送り先を組み合わせる。

## 受入条件

初期配置のボタンで挿入・抽出を実行。キーでもIn/OutはI/O、挿入はカンマ、上書きはピリオド、Match FrameはFで同じ編集を再現。

## 例外と復旧

素材が未選択、または選択した種類のストリームがなければ該当操作を無効にし、既存範囲を消さない。

## 参照資料と確認項目

- [A087](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/gang-source-and-program-monitor.html)　時刻の異なる二つのモニターを連動し、片方を5フレーム進めたときに両方の元の時間差が維持されるか試す。（公開手順）
