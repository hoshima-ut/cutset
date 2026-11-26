# 内容による素材検索の要件（IO-21）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

属性、発言、映像、音で場面を探し、候補から原本の一致箇所を再生する。

## 受入条件

同じ素材内に似た場面を2箇所作る。各結果のIn/Out、発言の文字列一致、撮影日による絞り込みを別々に確認。個人名による顔認識は想定しない。

## 例外と復旧

文字起こし未生成と該当なしを区別する。解析途中に手編集した素材は旧位置に無条件でジャンプしない。

## 参照資料と確認項目

- [A145](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/media-intelligence-and-search-panel.html)　解析前後の検索パネルを比較し、映像・音・発話・メタデータのどの情報を根拠に候補が表示されたか確かめる。（25.6正式告知で音声内容・類似画検索に対応。「映像のみ」とするFAQとの不一致あり）
- [A146](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/search-for-media-using-ai-powered-media-intelligence.html)　ファイル名に含まれない映像内容を入力し、返った区間の原画を再生して該当・非該当を判定する。（公開手順）
- [A147](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/search-for-audio-using-media-intelligence.html)　歓声と拍手が入った素材を用意し、音で検索できる版かを照合して、返った時間範囲を実際に聞き分ける。（25.6正式版の音声内容検索を継承。26.5の音声検索結果再生の不具合修正も根拠）
- [A148](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/search-for-similar-visuals-using-media-intelligence.html)　参照となる1フレームを選び、類似画検索を備える版で構図が近い別カットへ移動できるか確認する。（25.6正式版の類似フレーム検索を継承）
- [A149](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/manage-media-intelligence-metadata.html)　解析メタデータと素材を別端末へ移し、既存索引の再利用または必要な再解析を画面で判別できるか試す。（公開手順）

## 言葉・音・参照フレームから探す

映像の説明、聞こえる音の説明、発話の文字列、素材の属性から探せる。選択した1フレームから構図の近い別カットも探せる。結果ごとに一致した情報の種類と原本の時刻を表示し、試写できる。

[Premiere 26.x との照合](../../premiere-releases-2026-11.md)
