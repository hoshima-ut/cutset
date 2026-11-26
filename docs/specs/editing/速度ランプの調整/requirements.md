# 速度ランプの調整の要件（ED-56）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

速度線とキーの位置・ランプ長を操作し、速度変化を試聴する。

## 受入条件

100%から200%への急変と滑らかな加速を作り、同じ3点の素材フレーム番号、加速区間、終了位置を比較する。

## 例外と復旧

ランプが隣のキーを越える操作は許容幅に制限し、負の区間やキーの順序逆転を発生させない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-and-duration-using-time-remapping.html)
