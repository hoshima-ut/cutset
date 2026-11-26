# ED-24 入れ子と簡略版 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

子シーケンスを参照配置するか展開し、受け渡し用の簡略コピーを作る。

## 受入条件

子で変えた内容は親で再生される。簡略化で消した要素は元シーケンスには残る。

## 例外と復旧

循環参照を作る挿入を拒否する。子が欠落した場合はその区間とIDを保持したオフライン配置として開く。

## 参照資料と確認項目

- [A268](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/simplify-sequence.html)　簡易化コピーで無効クリップと空きトラックを除き、元のシーケンスと比較して除去対象だけが消えたか確かめる。（公開手順）
- [A319](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-nested-sequences/about-nested-sequences.html)　同じ子シーケンスを2箇所に使い、子を編集して両方に変更が反映されるかと各配置の尺を確かめる。（公開手順）
- [A320](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-nested-sequences/nest-a-sequence-in-another-sequence.html)　子シーケンスを親へ一つのネストとして置く場合と個別クリップとして置く場合で、後から動かせる単位を比較する。（公開手順）
- [A321](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-nested-sequences/reveal-a-clip-in-a-nested-source-sequence.html)　親で表示中のフレームからネスト元を開き、階層をまたいでもその瞬間に使われる正しい素材と時刻を特定する。（公開手順）
