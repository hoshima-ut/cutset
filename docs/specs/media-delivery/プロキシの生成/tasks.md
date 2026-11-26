# プロキシの生成の作業・試験（IO-24）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 実装と検証

ハーネスの作業IDは `BUILD-IO-24`、受入IDは `AC-IO-24`。

- [ ] 関連する上流部品の挙動と、設計に追加した条件の差分を確認する。
- [ ] [状態遷移とデータ境界](design.md)を実装経路で照合し、不足分を実装する。
- [ ] 下の入力で結果を照合し、[例外と復旧](requirements.md#例外と復旧)のケースを再現する。実行した版と結果を記録する。

## 具体的な試験

2素材のうち片方を生成中に差し替える。未変更の素材だけが自動接続され、失効した依頼は理由付きで再生成できる。

## 既存テストとの対応

ソースで確認した試験の入口。機能全体の合格判定はこのページの具体例で行う。

- [attach_checks_duration_and_export_ignores_proxies](../../../../crates/engine/src/proxies_tests.rs#L108) は <code>media.attachProxies</code> を呼ぶ。
- [create_attach_toggle_renders_the_same_picture](../../../../crates/engine/src/proxies_tests.rs#L33) は <code>media.createProxies</code> を呼ぶ。
- [generated_proxy_attaches_when_the_stored_duration_is_too_long](../../../../crates/engine/src/proxies_tests.rs#L423) は <code>media.createProxies</code> を呼ぶ。
