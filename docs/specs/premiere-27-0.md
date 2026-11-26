# Premiere 27.0 の新機能とCutsetの設計

2026年11月27日確認。Adobeが11月9日に更新した日本語版「新機能」の27.0欄には18項目がある。下表は各項目を既存のCutset機能に対応付け、照合前（`eef8094d`）に書かれていた内容と今回補った設計を示す。各機能の「作業・試験」には入力例と期待結果がある。実装と実機での合否は今後記録する。[Adobe公式の新機能](https://helpx.adobe.com/jp/premiere/desktop/whats-new/whats-new.html) ・ [26.xとAREA記事の照合](premiere-releases-2026-11.md)

| Adobeの機能に対応する作業 | 照合前のCutset仕様 | Cutsetの設計・受入試験 |
| --- | --- | --- |
| [編集からカラーへ切り替える](https://helpx.adobe.com/jp/premiere/desktop/correct-color/color-mode-fundamentals/color-mode-basics.html) | 作業面間で案件とシーケンスを共有。カラー移行の条件がなかった。 | [設計](editing/作業の切替/design.md#premiere-27-1) ・ [試験](editing/作業の切替/tasks.md#premiere-27-1) |
| [案件を参照して操作を提案するAI](https://helpx.adobe.com/jp/premiere/desktop/premiere-ai-assistant/overview.html) | 時間範囲の編集提案とUndoは既定。案件に対する質問と一括変更の境界は不明瞭。 | [設計](ai-plugin/変更提案のプレビュー/design.md#premiere-27-2) ・ [試験](ai-plugin/変更提案のプレビュー/tasks.md#premiere-27-2) |
| [タイムラインの指定範囲に静止画を生成する](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/edit-with-generative-ai/generate-media-with-generative-media-tool.html) | 素材の来歴と採用は既定。静止画の生成先は版の注記のみ。 | [設計](ai-plugin/生成素材の来歴/design.md#premiere-27-3) ・ [試験](ai-plugin/生成素材の来歴/tasks.md#premiere-27-3) |
| [音楽生成と映像に同期する効果音](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-music-to-your-timeline.html) | 版別の音楽生成と同期への言及あり。採用時の時刻の扱いが不足。 | [設計](ai-plugin/生成素材の来歴/design.md#premiere-27-4) ・ [試験](ai-plugin/生成素材の来歴/tasks.md#premiere-27-4) |
| [映像に合わせて環境音をレイヤー生成する](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-soundscape-to-your-timeline.html) | 追加できる版の注記あり。個々のレイヤーの編集を未定義。 | [設計](ai-plugin/生成素材の来歴/design.md#premiere-27-5) ・ [試験](ai-plugin/生成素材の来歴/tasks.md#premiere-27-5) |
| [会話音声の成分別調整](https://helpx.adobe.com/jp/premiere/desktop/add-audio-effects/adjust-volume-and-levels/apply-enhance-audio-to-clips.html) | 原音比較と混合比は既定。成分ごとの制御と保存が不足。 | [設計](audio/音声明瞭化/design.md#premiere-27-6) ・ [試験](audio/音声明瞭化/tasks.md#premiere-27-6) |
| [重なって話す二人の声を分離する](https://helpx.adobe.com/jp/premiere/desktop/add-audio-effects/basic-audio-editing/separate-overlapping-speakers.html) | 会話の明瞭化は既定。二人分の独立出力は設計が不足。 | [設計](audio/音声明瞭化/design.md#premiere-27-7) ・ [試験](audio/音声明瞭化/tasks.md#premiere-27-7) |
| [編集に追従する自動ダッキング](https://helpx.adobe.com/jp/premiere/desktop/add-audio-effects/adjust-volume-and-levels/automatically-duck-audio.html) | 生成キーと手修正キーの区別は既定。再計算の契機が不足。 | [設計](audio/ダッキング/design.md#premiere-27-8) ・ [試験](audio/ダッキング/tasks.md#premiere-27-8) |
| [効果のサムネイルと素材上の試写](https://helpx.adobe.com/jp/premiere/desktop/add-video-effects/types-of-effects/about-effects-and-effects-panel.html) | 絞り込みは既定。動画プレビューと素材試写は資料上の注記。 | [設計](effects/効果の検索/design.md#premiere-27-9) ・ [試験](effects/効果の検索/tasks.md#premiere-27-9) |
| [Windows ARMでのGPU・AI処理](https://helpx.adobe.com/jp/x-productkb/multi/windows-arm-support.html) | コーデック処理の経路表示は既定。ARM64と推論の組み合わせが不足。 | [設計](media-delivery/ハードウェア処理/design.md#premiere-27-10) ・ [試験](media-delivery/ハードウェア処理/tasks.md#premiere-27-10) |
| [立体、階調、ぼかしの追加効果](https://helpx.adobe.com/jp/premiere/desktop/add-video-effects/types-of-effects/effects.html) | 個々の効果の資料や旧版は登録済み。今回の追加セットの受入が不足。 | [設計](effects/効果の検索/design.md#premiere-27-11) ・ [試験](effects/効果の検索/tasks.md#premiere-27-11) |
| [プロパティで映像・音声効果とマスクを調整する](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/intro-to-editing/edit-video-using-the-properties-panel.html) | 追加・並べ替えは既定。簡易カードと詳細表示の同期が不足。 | [設計](effects/配置の効果スタック/design.md#premiere-27-12) ・ [試験](effects/配置の効果スタック/tasks.md#premiere-27-12) |
| [HSLマスクと他のマスクを組み合わせる](https://helpx.adobe.com/jp/premiere/desktop/add-video-effects/work-with-masks/create-masks-using-hsl-and-luminance.html) | HSL抽出とマット表示は既定。他マスクとの積集合の検証が不足。 | [設計](color/二次補正/design.md#premiere-27-13) ・ [試験](color/二次補正/tasks.md#premiere-27-13) |
| [追跡マスクの保存と復元](https://helpx.adobe.com/jp/premiere/desktop/add-video-effects/work-with-masks/mask-tracking-tools.html) | 手修正アンカーとキャッシュは既定。ファイル移動と復元後の品質検証が不足。 | [設計](effects/被写体の追跡/design.md#premiere-27-14) ・ [試験](effects/被写体の追跡/tasks.md#premiere-27-14) |
| [トランジションに足りないフレームを生成する](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-overview.html) | 前後の素材余白の算出は既定。不足時の生成と同意が未定義。 | [設計](editing/切替と素材余白/design.md#premiere-27-15) ・ [試験](editing/切替と素材余白/tasks.md#premiere-27-15) |
| [録音中の波形をタイムラインに表示する](https://helpx.adobe.com/jp/premiere/desktop/organize-media/import-files/record-a-voice-over-on-an-audio-track-from-the-timeline.html) | 収録停止後の波形を規定。録音中の表示が不足。 | [設計](audio/タイムラインでの収録/design.md#premiere-27-16) ・ [試験](audio/タイムラインでの収録/tasks.md#premiere-27-16) |
| [素材とタイムラインでiXMLを表示する](https://helpx.adobe.com/jp/premiere/desktop/get-started/preferences-and-settings/media-preferences.html) | 属性と書込先は既定。両画面で同じ録音情報を引く条件が不足。 | [設計](media-delivery/メタデータ/design.md#premiere-27-17) ・ [試験](media-delivery/メタデータ/tasks.md#premiere-27-17) |
| [音声の時間伸縮方式と音程を選ぶ](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-using-the-speedduration-option.html) | 速度と音程保持は既定。伸縮方式と独立した音程調整が不足。 | [設計](editing/速度・逆再生/design.md#premiere-27-18) ・ [試験](editing/速度・逆再生/tasks.md#premiere-27-18) |

## 個別に確認が必要な点

- **生成ツールの提供状態**　27.0の機能一覧は画像、音楽、効果音、サウンドスケープを案内している。日本語の生成ツール操作手順には「Beta」の表記がある。音楽とサウンドスケープの個別の英語手順では11月10日更新時に同表記を確認できなかった。Cutsetはサービスごとの利用条件を表示する。[生成ツールの手順](https://helpx.adobe.com/jp/premiere/desktop/edit-projects/edit-with-generative-ai/generate-media-with-generative-media-tool.html) ・ [音楽](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-music-to-your-timeline.html) ・ [サウンドスケープ](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-soundscape-to-your-timeline.html)
- **追加エフェクトの内訳**　Adobeの新機能ページとリリース告知は8種のうち5種を例示している。残り3種は名称と追加版を対応付けられる一次資料が見つかるまで未特定とする。[Adobeの27.0告知](https://community.adobe.com/announcements-727/welcome-to-adobe-premiere-27-0-1655028)

## 版別リリースノートの追加差分

リリースノートには、上の18項目に加えて環境設定、対応形式、機材要件の変更もある。以下はCutsetの調査・検証対象。特定機材の対応表を更新するには、試料と実際に使った処理経路を記録する。[Adobe 27.0のリリースノート](https://helpx.adobe.com/jp/premiere/desktop/whats-new/release-notes.html)

| 確認する差分 | Cutsetでの確認先と試験 |
| --- | --- |
| ドラッグ中のリップルトリムの表示設定 | [リップルトリム](editing/リップルトリム/design.md)でドラッグ中のプレビューと離した時の反映を比較する。両モードの確定フレームとUndoの結果は同じになる。 |
| Windows ARM64のRTX推論、MXF内H.264・HEVCのGPU復号、GPUメモリ不足 | [ハードウェア処理](media-delivery/ハードウェア処理/design.md)で推論・復号を別々に記録する。メモリ不足では利用不能な操作、理由、代替経路を表示する。 |
| Sony FX5のX-OCN（LT・C1・C2）、ARM64の各社RAW、ALEXA 35 Xtreme | [カメラRAW](media-delivery/カメラRAW/design.md)で各形式と機種を個別に照合する。ARRIRAW・ARRICORE、Cinema RAW Light、R3D・R3D NE、N-RAWは試料ごとに画とメタデータを確認する。 |
| Sony RAW・16-bit linear F65 RAWのAdobe側の読み込み終了 | [形式と上限](media-delivery/形式と上限/design.md)では旧案件の原本参照と代替素材への再リンクを確認する。Cutset側の対応継続・終了はデコーダーと試料で判断する。 |
