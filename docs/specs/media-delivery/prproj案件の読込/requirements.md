# prproj案件の読込の要件（IO-57）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

Premiereで保存した案件ファイル（`.prproj`）をCutsetで直接開き、シーケンス・トラック・クリップの切り点・素材参照・マーカー・ビンを新しいCutset案件として再現する。XMLやAAFへ書き出す手間と、その過程で落ちる情報をなくす。原本は書き換えない。書き出し（`.prproj` の保存）は対象外で、読込の結果を見てから別に判断する。

## 受入条件

自社で作成した見本案件を開くと、各シーケンスのクリップの配置・In/Out・トラック・素材パスが、同じ案件からPremiereが書き出したFCP7 XMLを読み込んだ結果とフレーム単位で一致する。再現できなかった要素は種類・場所・件数を一覧に示し、原本のハッシュは読込の前後で変わらない。

## 例外と復旧

圧縮やXMLが壊れたファイル、未確認の保存版、暗号化・共同編集用の案件は理由を示して読み込まず、推測で変換しない。素材が見つからない場合はオフラインとして取り込み、既存の再リンクで復旧できる。一部の要素だけ再現できない場合は取り込みを続け、一覧に残す。大きすぎる・入れ子が深すぎるファイルは上限で打ち切り、途中の案件を保存しない。

## 参照資料と確認項目

- 上流の課題 G2（`docs/reference/filmcraft/gaps.md`）と要望 storytold/filmcraft#5296。形式の公開仕様はない。構造は[クリーンルーム規約](https://github.com/storytold/craft-contrib/blob/main/standards/clean-room.md)の「見本ファイル」の条件を満たす自社作成の案件からのみ学ぶ。
- Premiereの公開手順で、案件の保存版と旧版での開き方を確認する。[案件の後方互換](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/backward-compatibility-of-projects.html)
