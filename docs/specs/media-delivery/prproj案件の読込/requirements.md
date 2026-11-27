# prproj案件の読込の要件（IO-57）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

Premiereで保存した案件ファイル（`.prproj`）をCutsetで直接開き、シーケンス・トラック・クリップの切り点・素材参照・マーカー・ビンを新しいCutset案件として再現する。Premiere側でXMLを書き出す手間と、XMLで落ちる情報を減らす。原本は書き換えない。[編集ソフト間の引き継ぎ](../../workflow/編集ソフト間の引き継ぎ/requirements.md)のH1判定で着手が決まった場合に実装する。書き出しは[IO-58](../prproj案件の書き出し/requirements.md)。

## 受入条件

自社で作った見本を開くと、各シーケンスが[照合の基準](design.md#照合の基準)で、同じ案件からPremiereが書き出したXMLの読込結果と一致する。ビン・ラベル色・効果の値は作成票の値と許容差内で一致する。再現できなかった要素は要素キー・場所・件数つきで取込報告に出る。原本のsha256と更新日時は読込の前後で変わらない。

## 例外と復旧

壊れた圧縮・XML、上限を超える入力、未確認の版、想定外のルート要素は、案件を作らずに理由を返し、Premiere側でXMLを書き出して開く経路を案内する。推測で変換しない。素材が見つからない場合はオフラインとして取り込み、既存の再リンクで復旧できる。一部の要素だけ再現できない場合は取り込みを続けて報告に残す。暗号化や共同編集用の案件は、見本ができるまで「想定外のルート要素」として扱う。

## 参照資料と確認項目

- 上流の課題 G2（`docs/reference/filmcraft/gaps.md`）と要望 storytold/filmcraft#5296。形式の公開仕様はない。構造は[クリーンルーム規約](https://github.com/storytold/craft-contrib/blob/main/standards/clean-room.md)の見本ファイルの条件を満たす自社作成の案件からのみ学ぶ。
- Premiereの公開手順で、案件の保存版と旧版での開き方を確認する。[案件の後方互換](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/backward-compatibility-of-projects.html)
