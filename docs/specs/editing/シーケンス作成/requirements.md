# シーケンス作成の要件（ED-09）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

プリセットまたは素材からタイムベースと画面寸法を設定する。

## 受入条件

横長素材を縦シーケンスに配置し、再開後も縦の納品設定と素材の原寸が両立する。

## 例外と復旧

異なるレートの素材を初めて置く場合は、シーケンス設定を変更するか保持するか選んだ後に配置する。

## 参照資料と確認項目

- [A251](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/create-a-sequence.html)　縦動画用の新規シーケンスと素材から作ったシーケンスを用意し、初期寸法・時間軸・音声構成を比較する。（公開手順）
- [A254](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/change-sequence-settings.html)　既存シーケンスの寸法を変え、配置した素材の元寸法とタイムラインのカット位置が維持されるか試す。（公開手順）
- [A255](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/sequence-settings-reference.html)　シーケンスでタイムベース、フィールド、ピクセル比、音声レート、プレビュー形式を読み戻し、設定表と比較する。（公開手順）
- [A256](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/sequence-presets-and-settings.html)　配布プリセットを二つ使い、プリセット名だけでなく実際に生成されたシーケンスの各値を比較する。（公開手順）
- [A257](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/create-a-custom-sequence-preset.html)　独自のフレーム寸法と音声設定をプリセット保存し、別の新規案件でも同じ組み合わせを呼び出せるか試す。（公開手順）
