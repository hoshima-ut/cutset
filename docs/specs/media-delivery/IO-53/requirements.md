# IO-53 XML交換 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

編集交換用XMLの方言と対象バージョンを識別し、配置を書き出し・読み戻し照合する。

## 受入条件

フェード、音量・パン、ネスト、テキスト、効果の各例を、変換ログと相手側の実データに分けて記録。

## 例外と復旧

未対応の版・タグ・効果は対象項目を示す。不明な方言を別形式として推測変換しない。

## 参照資料と確認項目

- [A135](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/migrate-from-final-cut-pro-x.html)　FCPXMLと旧FCP XMLを区別し、対応する変換経路を使った際の尺・配置・変換警告を比較する。（公開手順）
- [A176](https://helpx.adobe.com/premiere/desktop/organize-media/transfer-files/supported-elements-for-final-cut-pro-x.html)　FCP X経由でカット、速度変更、タイトルを含む同一案件を往復させ、編集可能・要修正の項目を列挙する。（公開手順）
- [A649](https://helpx.adobe.com/premiere/desktop/render-and-export/export-files/export-a-project-as-a-final-cut-pro-xml-file.html)　フェード、ネスト、音量調整を含むXMLを相手側で開き、変換ログと消えた調整を対応付ける。（公開手順）
