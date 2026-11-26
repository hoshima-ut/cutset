# GR-04 動くタイトル — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

文字と図形の変形をキーフレーム化し、スクロールの前後余白と静止を指定する。

## 受入条件

ロールを長くしたときの読める速度と開始端・終了端を確認する。

## 例外と復旧

静止区間の合計が配置尺を超える設定は、必要な最短尺を表示して確定を止める。書体の変化で高さが変われば再計算する。

## 参照資料と確認項目

- [A348](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/create-credit-rolls.html)　最初と最後を画面外にした名簿を流し、冒頭・末尾で文字が途中から出入りしないか再生する。（公開手順）
- [A350](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/animate-layers-using-the-effect-controls-panel.html)　Effect Controlsで図形に二つの位置キーを置き、開始・中間・終了の座標を確認する。（公開手順）
- [A351](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-images-and-graphics/animate-layers-using-properties-panel.html)　Propertiesでレイヤーの値を時間を変えて設定し、同じ時間のキーを再選択して変更できるか試す。（公開手順）
