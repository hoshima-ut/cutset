# 入力チャンネル割当の要件（AU-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

入力チャンネルとモノ、ステレオ、多チャンネルの出力の対応を設定する。

## 受入条件

左に声・右に基準音を入れ、素材解釈、シーケンスのミックス、書き出しファイルを順に確認する。

## 例外と復旧

存在しない入力番号や互換性のない出力を示して確定を止める。元素材の音声データを変換せず、対応表を変更して復旧できる。

## 参照資料と確認項目

- [A498](https://helpx.adobe.com/premiere/desktop/add-audio-effects/basic-audio-editing/audio-editing-concepts.html)　クリップ、トラック、ミックスのレベルを別々に変え、対象外の経路のメーター値を確認する。（公開手順）
- [A513](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/audio-channel-mapping.html)　左右が異なる音声素材のチャンネル対応を変更し、再生される側を出力メーターで確認する。（公開手順）
- [A516](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/map-source-audio-channels-on-import.html)　読み込み前に素材のチャンネル解釈を指定し、新しく取り込んだ素材の各出力を確認する。（公開手順）
- [A517](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/change-source-audio-channel-mapping.html)　読込済み素材のソース割当を入れ替え、新たに配置したクリップの左右をテスト音で識別する。（公開手順）
- [A519](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/break-a-stereo-track-into-mono-tracks.html)　片側だけに声のあるステレオ素材をモノに分け、二つのモノ項目の片方だけが鳴るか試す。（公開手順）
- [A520](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/use-mono-clips-as-stereo-clips.html)　一つのモノ素材をステレオとして割り当て、左右へ送られた波形と位相を照合する。（公開手順）
- [A521](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/edit-a-multi-clip-link-in-the-source-monitor.html)　複数リンクした音声をSource Monitorに開き、一構成要素だけを選ぶ操作と全体選択を比較する。（公開手順）
- [A524](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/assign-multiple-audio-channels.html)　各チャンネルで異なる数字を読む素材を複数出力へ割り当て、書き出し後に発話の順序を照合する。（公開手順）
