# 配置の効果スタックの作業・試験（FX-02）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-FX-02`、受入IDは `AC-FX-02`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

左半分だけ白い画像に水平反転と左半分の切り抜きを置く。順序で残る白領域が変わり、隣の未選択配置は両方の試行で元の画像と一致する。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [a_clip_without_a_duration_still_draws](../../../../crates/ui-egui/src/panels/effect_controls.rs#L1782) は <code>effects.toggleAnimation</code> を呼ぶ。
- [paste_attributes_with_scaled_keyframes_and_remove_attributes](../../../../crates/engine/src/clip_ops_tests.rs#L139) は <code>edit.pasteAttributes</code> を呼ぶ。
- [default_audio_transition_is_used_by_apply](../../../../crates/engine/src/mixer_tests.rs#L403) は <code>effects.setDefaultTransition</code> を呼ぶ。

<a id="effect-and-mask-properties"></a>

## プロパティで映像・音声効果とマスクを調整する

- [ ] 映像と音声を含む配置でマスクの値を変え、詳細画面で確認する。Undoを1回行い両画面とプレビューが同時に戻る。
