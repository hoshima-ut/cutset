# 機能仕様の照合範囲

2026-11-26時点の照合です。製品台帳の全IDに要件・設計・作業が揃っているか、上流コード・コマンド・既存テストのどれを参照できるかを分野ごとに集計しました。各件数は機能単位で、列どうしは重なります。

| 分野 | 仕様 | 上流コードの参照あり | 関連コマンドあり | 関連テストの参照あり | 部分実行の記録あり¹ | 上流対応を要確認 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| [ワークスペース](../specs/workspace/README.md) | 20 | 18 | 6 | 14 | 0 | 3 |
| [素材管理と納品](../specs/media-delivery/README.md) | 56 | 43 | 24 | 40 | 0 | 10 |
| [タイムライン編集](../specs/editing/README.md) | 59 | 53 | 30 | 52 | 2 | 2 |
| [エフェクト](../specs/effects/README.md) | 21 | 17 | 7 | 18 | 0 | 4 |
| [カラー](../specs/color/README.md) | 10 | 10 | 5 | 10 | 0 | 0 |
| [グラフィック](../specs/graphics/README.md) | 8 | 8 | 5 | 8 | 0 | 0 |
| [字幕](../specs/captions/README.md) | 4 | 4 | 3 | 4 | 0 | 0 |
| [音声](../specs/audio/README.md) | 18 | 15 | 7 | 15 | 0 | 3 |
| [メニューと文脈操作](../specs/commands/README.md) | 35 | 30 | 0 | 27 | 0 | 4 |
| [編集ワークフロー](../specs/workflow/README.md) | 14 | 6 | 0 | 6 | 0 | 0 |
| [AIと拡張](../specs/ai-plugin/README.md) | 9 | 9 | 1 | 9 | 1 | 0 |
| [ブラウザ](../specs/browser/README.md) | 5 | 5 | 0 | 4 | 0 | 0 |
| 合計 | 259 | 218 | 88 | 207 | 3 | 26 |

¹ この表で機能IDに対応付けた実行記録は、固定候補の試聴計画、デモ案件のマーカー追加、Undo/Redoです。719命令の照合は登録情報（ID・表示名・メニュー・既定キー・引数）の検査です。既存テストの参照には、関連するモジュール、または関連命令を直接呼ぶテストを記載しています。テストの掲載だけで合格とは判定しません。

実装済みの範囲は各設計書の既存実装欄、追加する処理は状態遷移・処理境界、今後の確認は各作業表に記載しています。人の試聴、外部製品との往復、提供元との実認証、OS・ブラウザ間の差異は個別の環境で確認します。公開資料813件にはベータ・他版・背景資料も含まれます。Premiere 26.xの全内部仕様との一致は未確認です。

[機能索引](../specs/index.md) ・ [試聴計画の検証](../development/progress.md) ・ [マーカーと履歴の再現手順](marker-history.md)

## 上流対応を引き続き確認する機能

前回未確認だった41件のうち、15件で再利用できる実装を関数単位で確認しました。以下の機能は、既存実装が要件のどこまでを満たすかを判断する作業が残っています。コード参照の件数には、新規設計で接続先として参照する周辺部品も含みます。

- [UI-13 キーボードと支援技術](../specs/workspace/UI-13/design.md)
- [UI-18 球面映像の試聴](../specs/workspace/UI-18/design.md)
- [UI-19 HDRの監視](../specs/workspace/UI-19/design.md)
- [IO-03 分割収録の取り込み](../specs/media-delivery/IO-03/design.md)
- [IO-14 施設入出力](../specs/media-delivery/IO-14/design.md)
- [IO-21 内容による素材検索](../specs/media-delivery/IO-21/design.md)
- [IO-22 類似フレーム検索](../specs/media-delivery/IO-22/design.md)
- [IO-33 中間素材への置換](../specs/media-delivery/IO-33/design.md)
- [IO-37 共有素材・利用権](../specs/media-delivery/IO-37/design.md)
- [IO-38 外部ツールとの往復](../specs/media-delivery/IO-38/design.md)
- [IO-45 再圧縮の回避](../specs/media-delivery/IO-45/design.md)
- [IO-49 配信と来歴](../specs/media-delivery/IO-49/design.md)
- [IO-50 遠隔モニタリング](../specs/media-delivery/IO-50/design.md)
- [ED-39 没入型の編集](../specs/editing/ED-39/design.md)
- [ED-56 速度ランプの調整](../specs/editing/ED-56/design.md)
- [FX-03 原本と配置の効果](../specs/effects/FX-03/design.md)
- [FX-18 旧効果の読み戻し](../specs/effects/FX-18/design.md)
- [FX-20 時間効果](../specs/effects/FX-20/design.md)
- [FX-21 球面効果](../specs/effects/FX-21/design.md)
- [AU-09 音声明瞭化](../specs/audio/AU-09/design.md)
- [AU-16 指定語の消音・置換音](../specs/audio/AU-16/design.md)
- [AU-17 試聴の一括消音](../specs/audio/AU-17/design.md)
- [MN-08 外部音声編集への送出](../specs/commands/MN-08/design.md)
- [MN-13 中間レンダーと復帰](../specs/commands/MN-13/design.md)
- [MN-24 ガイドの転用](../specs/commands/MN-24/design.md)
- [MN-33 表示フレームでの検索](../specs/commands/MN-33/design.md)
