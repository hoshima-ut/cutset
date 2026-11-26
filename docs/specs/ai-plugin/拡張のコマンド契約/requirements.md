# 拡張のコマンド契約の要件（AI-06）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

操作・入力型・対象・失敗理由を列挙し、公式AIと拡張に同じ編集経路を提供する。

## 受入条件

非対応の命令は理由付きで返し、手操作と同じUndo単位、ロック、素材アクセス範囲を守る。

## 例外と復旧

未知の命令、型不正、許可外のファイル操作には機械可読な理由を返す。汎用のバッチ実行を一括Undoが保証される取引として扱わない。

## 参照資料と確認項目

- [A737](https://helpx.adobe.com/premiere/desktop/premiere-ai-assistant/customize-ai-assistant-with-skills.html)　27系の比較試験で自作スキルを選び、同じ指示を通常実行した場合との提案・編集範囲の違いを観察する。（27.0正式のAI Assistant。26系正式の対象外）
