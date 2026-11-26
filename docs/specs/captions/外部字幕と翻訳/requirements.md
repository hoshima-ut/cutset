# 外部字幕と翻訳の要件（CC-03）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

言語・規格ごとのトラックを読み込み、翻訳候補を別トラックで校正する。

## 受入条件

言語切替時に同時刻の二つのトラックが混同されず、人名の修正が原文に波及しない。

## 例外と復旧

同一トラック上で重なる区間や読めない時刻行は該当箇所を示し、修正または取込中止を選べる。対応外装飾は取込結果に表示する。

## 参照資料と確認項目

- [A376](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/translate-captions.html)　日本語字幕を別言語へ翻訳し、結果を修正でき、原文を選び直せるか確かめる。（公開手順）
- [A378](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/supported-file-formats-for-captions.html)　同じ時刻のSRTと放送用字幕を読み込み、形式ごとの本文・時間・チャンネル情報を比較する。（公開手順）
- [A379](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/import-caption-file-from-third-party-service.html)　外部で作った字幕をタイムライン途中へ置き、最初と最後の表示時刻が予定どおりか見る。（公開手順）
- [A380](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/download-language-packs-from-creative-cloud.html)　Creative Cloud経由で追加した言語をPremiereで選び、その言語の短いクリップを書き起こす。（公開手順）
- [A381](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/language-packs-for-teams-and-enterprise-users.html)　組織配布の検証端末で言語パックの配備状態を確認し、一般ユーザーで対象言語の認識を試す。（公開手順）
- [A382](https://helpx.adobe.com/premiere/desktop/add-text-images/insert-captions/download-language-packs-from-within-premiere.html)　Premiere内で未取得の言語を指定し、取得完了後に再起動して同じ言語を選べるか試す。（公開手順）
