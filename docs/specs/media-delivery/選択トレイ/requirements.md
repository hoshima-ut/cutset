# 選択トレイの要件（IO-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

複数素材の順番・除外・取り込み方法を確定前に変更する。

## 受入条件

使う順が撮影順と異なる3本を選び、1本だけ除外。参照取り込みと複製取り込みで、案件項目数とディスク上の複製数を別々に照合。

## 例外と復旧

確定直前に読めなくなった候補を示す。既に処理した項目と再試行対象を識別し、再試行で二重登録しない。

## 参照資料と確認項目

- [公開資料 1](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/create-new-project.html)
