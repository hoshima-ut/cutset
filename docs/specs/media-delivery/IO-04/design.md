# IO-04 取り込み処理 — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

原本参照、複製、変換、代理生成から必要な処理を選び、保存先を確定して処理状況を表示する。

## データと処理境界

取り込み元、検証済みコピー、変換物、代理素材の対応を保存する。コピー検証を選んだ場合は照合完了後に新しい参照先へ切り替える。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M5](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/media_browser.rs](../../../../crates/engine/src/media_browser.rs)。

既存CLIで列挙できる関連命令。引数とメニューは実バイナリで照合済み。挙動の確認方法は作業表に記載する。

| 命令 | 入力 | 定義・登録の参照先 |
| --- | --- | --- |
| <code>file.import</code> | <code>{"paths":[str],"bin":binId?,"imageSequence":bool?,"replace":bool?}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.importDemoFootage</code> | <code>{"scene":"OceanSunset&#124;Aurora&#124;CityNight&#124;Dunes&#124;Plasma&#124;Forest"}</code> | [commands.rs](../../../../crates/engine/src/commands.rs) |
| <code>file.importFromMediaBrowser</code> | <code>{"paths":[str]?,"imageSequence":bool?}</code> | [project_tools.rs](../../../../crates/engine/src/project_tools.rs) |
| <code>mediaBrowser.clearRecent</code> | <code>{}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.favorite</code> | <code>{"path":str?,"remove":bool?}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.import</code> | <code>{"paths":[str]?,"bin":binId?,"imageSequence":bool?}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.list</code> | <code>{"path":str?,"fileTypes":str?}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.navigate</code> | <code>{"path":str} &#124; {"back":true} &#124; {"forward":true} &#124; {"up":true}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.openInSource</code> | <code>{"path":str?}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.probe</code> | <code>{"path":str}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.roots</code> | <code>{}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.select</code> | <code>{"paths":[str]}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>mediaBrowser.settings</code> | <code>{"fileTypes":"all&#124;video&#124;audio&#124;image&#124;project&#124;caption&#124;&lt;ext&gt;"?,"view":"list&#124;thumbnails"?,"columns":[str]?,"columnWidths":{str:f32}?,"importAsImageSequence":bool?,"hoverScrub":bool?,"thumbnailSize":f32?}</code> | [media_browser.rs](../../../../crates/engine/src/media_browser.rs) |
| <code>project.ingestSettings</code> | <code>{"enabled":bool?,"action":"copy&#124;transcode&#124;createProxies&#124;copyAndCreateProxies"?,"destination":str?,"preset":str?}</code> | [proxies.rs](../../../../crates/engine/src/proxies.rs) |

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
