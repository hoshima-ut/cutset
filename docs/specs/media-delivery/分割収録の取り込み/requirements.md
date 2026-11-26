# 分割収録の取り込みの要件（IO-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

同じテイクのファイル群を論理クリップとして扱い、カードの構造を保った複製を作れる。

## 受入条件

2ファイルにまたがるテイクの境界を再生し、映像の欠落・音声の二重再生・時刻の跳びを記録。

## 例外と復旧

中間ファイルが不足したときは不連続の位置を示す。同じ名前だけを理由に別カードの断片を連結しない。

## 参照資料と確認項目

- [A174](https://helpx.adobe.com/premiere/desktop/organize-media/transfer-files/transfer-assets-from-file-based-media.html)　複数ファイルに分割された収録カードをディレクトリごと複写し、全尺と継ぎ目の音声を原本と比較する。（公開手順）
