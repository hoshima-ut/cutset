# 拡張ホストの要件（IO-39）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

対応ホスト版と権限を宣言した拡張に編集命令を公開し、不在の拡張を案件内で特定する。

## 受入条件

拡張を外して同じ案件を開くと、不足する能力と影響箇所が分かる。未実行の命令は未対応理由を返し、原本と配置を保持する。

## 例外と復旧

拡張が不在または非互換なら対象の機能を停止し、保持したパラメーターを再導入後に復元できるようにする。

## 参照資料と確認項目

- [A750](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/third-party-plugins-cause-premiere-to-crash.html)　不調な外部プラグインを読み込まない起動で案件へ到達し、対象効果の欠落を表示する。（障害診断）
- [A789](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/install-plug-ins-and-extensions.html)　新しい検証用パネルを追加し、再起動後の起動場所とアンインストール後の表示を確かめる。（公開手順）
- [A790](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/plug-ins.html)　同じ処理に必要なサードパーティ製の効果と入出力拡張を分け、対応OS・ホスト版・無効時の挙動を記録する。（公開手順）
