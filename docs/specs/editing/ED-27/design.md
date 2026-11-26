# ED-27 リップルトリム — 設計

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 操作と状態遷移

リップル対象の端を選び、動く後続と同期対象を表示して変更量を確定する。

## データと処理境界

実際に動かせる端の差分を先に解き、後続の配置と同期対象の字幕へ同じ量を伝播する。素材時間とシーケンス時間を別に扱う。

## 既存実装との対応

方針は「既存部品を利用」。対象マイルストーンは[M2](../../../development/milestones.md)。

上流コードの照合先：[crates/engine/src/trim.rs](../../../../crates/engine/src/trim.rs)、[crates/edit/src/lib.rs](../../../../crates/edit/src/lib.rs)。

確認した関数：[ripple_trim_group](../../../../crates/edit/src/lib.rs)。対象全員のトラックロックと許容差分を先に調べ、グループ共通の差分で仮のシーケンスを編集する。音声と映像の境界がずれたケースに回帰試験がある。

編集画面・支援技術・エージェント操作の共通条件は[分野別の操作契約](../../shared/interaction.md)を適用する。
