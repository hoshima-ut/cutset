# 原本の解釈設定の要件（MN-31）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

元のバイト列を変えずにレート、画素比、フィールド、アルファを指定する。

## 受入条件

同じ素材を二度使い、解釈変更の反映範囲と尺を、片方の配置だけを変更した場合と比べる。

## 例外と復旧

複数選択で相反する元値を単一値として表示しない。安全に適用できない配置や尺不足を確認前に列挙する。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/edit-projects/modify-clip-properties/modifying-clip-properties-with-interpret-footage.html)
