# 設定の保存範囲の要件（UI-14）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

端末、案件、シーケンスに保存する設定を識別して変更・復元する。

## 受入条件

一般、外観、音声・音声機器、保存、共同制作、カラー、コントロールサーフェス、グラフィック、ラベル、素材・解析、メモリ、再生、タイムライン、トリムを対象に、ユーザー設定と案件設定を区別する。別案件・再起動で適用範囲を検査。

## 例外と復旧

旧版の設定に未知の項目や非対応デバイスがあれば利用可能な値で起動し、復元できなかった設定を一覧に残す。

## 参照資料と確認項目

- [A021](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/preferences-overview.html)　設定の作用先を利用者単位・案件単位・シーケンス単位に分け、再度開いて確認する。（公開手順）
- [A022](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/general-preferences.html)　起動時のホーム表示など一般設定を変え、既存案件の編集データが変わらない。（公開手順）
- [A023](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/appearance-preferences.html)　外観を切り替え、非アクティブとロック状態を高コントラストでも判別できる。（公開手順）
- [A031](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/graphics-preferences.html)　文字表示の既定を変え、既存のタイトルと新規作成したタイトルの差を記録する。（公開手順）
- [A032](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/labels-preferences.html)　ラベル色と名前を変更し、素材の識別とシーケンス上の色表示を比較する。（公開手順）
- [A033](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/media-preferences.html)　メディア環境設定変更後に新規素材を読み、同素材の既存配置への波及を調べる。（版混在。タイムライン・Sourceでの音声iXMLメタデータ表示の追加は27.0）
- [A037](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/timeline-preferences.html)　タイムラインの既定を変更して同じ操作を繰り返し、新規トラックの有無を比較する。（26.3で自動トラック追加設定、26.5でリップル表示設定。27.0の設定場所と区別）
- [A038](https://helpx.adobe.com/premiere/desktop/get-started/preferences-and-settings/trim-preferences.html)　トリム表示やステップ量の変更が結果の尺・更新タイミングにどう効くかを測る。（26.5でリップルトリム中の動的表示をオフにできる。27.0のTimeline設定と区別）
- [A766](https://helpx.adobe.com/premiere/desktop/troubleshooting/preferences-and-settings-issues/why-reset-preferences.html)　初期設定だけを変えた再試験で症状が消えるか確認し、素材破損と区別する。（障害診断）
- [A767](https://helpx.adobe.com/premiere/desktop/troubleshooting/preferences-and-settings-issues/reset-preferences-at-launch.html)　起動時に設定初期化を選び、処理対象を確認してユーザー配列を退避する。（障害診断）
- [A768](https://helpx.adobe.com/premiere/desktop/troubleshooting/preferences-and-settings-issues/reset-preferences-using-the-preferences-folder.html)　設定フォルダーを退避した状態で新規設定が生成され、元ファイルを再利用できる。（障害診断）
- [A769](https://helpx.adobe.com/premiere/desktop/troubleshooting/preferences-and-settings-issues/restore-preferences.html)　復元したカスタム配列・ワークスペースを再起動後に選択できる。（障害診断）
- [A770](https://helpx.adobe.com/premiere/desktop/troubleshooting/preferences-and-settings-issues/unable-to-migrate-settings-after-updating-premiere.html)　旧設定の移行に失敗した場合に該当項目を識別し、新しい既定値で案件を開く。（障害診断）
