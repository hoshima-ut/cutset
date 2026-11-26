# AU-11 音楽の尺合わせ — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

拍や区切りを基準に音楽を目標尺に近づけ、つなぎ目を試聴する。

## 受入条件

指定尺との差、曲の頭と終わり、ドラムや歌詞の継ぎ目を、単純な再生速度変更と区別して調べる。

## 例外と復旧

接続候補が見つからない、または保護区間の合計が目標尺を超えた場合は適用を保留する。元の曲の配置を保持して条件を変更できる。

## 参照資料と確認項目

- [A548](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/remix-audio-in-premiere.html)　Premiere内で楽曲を目標尺にリミックスし、再構成された箇所を原曲と聞き比べる。（公開手順）
- [A549](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/remix-tool-considerations-in-premiere.html)　拍の明瞭な曲と長い持続音の曲に同一の目標尺を与え、許容差と継ぎ目の聞こえ方を記録する。（公開手順）
- [A565](https://helpx.adobe.com/premiere/desktop/add-audio-effects/apply-audio-effects/remix-in-premiere.html)　リミックス済み音楽の目標尺をさらに変え、配置し直さなくても新しい構成を試聴できるか確かめる。（公開手順）
