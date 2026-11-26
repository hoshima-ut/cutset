# AI-08 生成素材の来歴 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

生成区間を独立素材として保存し、モデル・入力範囲・選択版を記録する。

## 受入条件

元映像の端を保ち、生成区間だけを外せる。再生・再書き出し時に生成モデルを呼び直さない。

## 例外と復旧

生成失敗やキャンセルでは元配置を変更しない。生成物欠落時は再リンクまたは明示した再生成を提案し、バックグラウンドで課金を発生させない。

## 参照資料と確認項目

- [A305](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-overview.html)　生成延長に対応する素材条件を対象ビルドで照合し、生成した余白とカメラが記録した範囲を区別して戻せるか試す。（26.5で素材解像度・FPS・HDR等を拡張。トランジションに不足するフレームの生成は27.0）
- [A306](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/add-frames-using-generative-extend.html)　短いクリップの末尾を延長して生成部分をトリムし直し、元の最終フレームと原ファイルが同一か調べる。（26.5で素材解像度・FPS・HDR等を拡張。トランジションに不足するフレームの生成は27.0）
- [A307](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-extend-faq.html)　拡張可能な尺、映像・音声の条件、利用資格を26系の版別に照合し、非対応の試料で理由を表示できるか確認する。（26.5で素材解像度・FPS・HDR等を拡張。トランジションに不足するフレームの生成は27.0）
- [A308](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/user-data-storage-for-model-output-feedback.html)　生成結果へのフィードバックの有無で送信される素材と利用条件の説明を、対象版の表示・公式資料と照合する。（公開手順）
- [A309](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-media-tool-overview.html)　生成映像・効果音が編集可能な素材として追加される版を確認し、生成した配置を独立して移動・削除できるか試す。（26.5正式は映像・効果音。静止画生成と映像同期の効果音は27.0）
- [A310](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generate-media-with-generative-media-tool.html)　生成内容と保存先を指定し、選んだ結果の追加、失敗時の既存タイムライン保持、版ごとのベータ表記を照合する。（26.5正式は映像・効果音。静止画生成と映像同期の効果音は27.0）
- [A311](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-media-tool-faq.html)　生成ツールの利用条件とクレジットの表示を対象26系で読み、確定前と取り消し後の扱いを記録する。（26.5正式は映像・効果音。静止画生成と映像同期の効果音は27.0）
- [A312](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generate-music-overview.html)　音楽生成の提供版・利用資格を26系のリリース記載と照合し、該当版のみ入力できる尺やスタイルを記録する。（27.0正式の音楽生成。26系正式の対象外）
- [A313](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-music-to-your-timeline.html)　対象ビルドに音楽生成がある場合は追加位置と曲尺を確認し、タイムライン上で短縮後も曲を独立に扱えるか試す。（27.0正式の音楽生成。26系正式の対象外）
- [A314](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generate-music-faq.html)　生成音楽の利用制約・対応期間・使用量表示について、提供開始版と該当しない26系の表示を対照する。（27.0正式の音楽生成。26系正式の対象外）
- [A316](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-soundscape-to-your-timeline.html)　サウンドスケープ追加の提供版を確認し、対応時だけ選択区間・音声トラックと生成後の長さを照合する。（27.0正式のサウンドスケープ生成。26系正式の対象外）
- [A317](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/generative-remove.html)　不要物の生成除去はベータ扱いとビルドを確認し、26系正式版と区別したうえで対応時の元素材保存を試す。（Generative Removeは公開ベータ。26系正式の対象外）
- [A318](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-with-generative-ai/add-generated-sound-effects-to-your-timeline.html)　効果音生成が提供される版で足音を一箇所に追加し、クリップの位置・長さ・再編集可能性を確認する。（26.5で効果音生成、素材映像への自動同期は27.0）
- [A740](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/iphone-hdr-clips-are-unsupported.html)　iPhone HDR素材を生成延長し、26.5の対応拡張と古い制限のどちらが対象構成で再現するか確認する。（2026年1月の回避策。26.5でHDR入力対応を拡張、機種・形式別に再確認）
- [A744](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/generative-extend-known-issues.html)　生成延長を対応外素材で試し、失敗しても元の端とトラック位置を保持する。（26.5で素材解像度・FPS・HDR等を拡張。トランジションに不足するフレームの生成は27.0）
