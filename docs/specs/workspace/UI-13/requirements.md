# UI-13 キーボードと支援技術 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

ポインターなしでトリム・字幕修正を完了し、読み上げで作用先と結果を確認する。

## 受入条件

一連のトリムと字幕修正をキーだけで完了する。フォーカス対象、押下状態、選択数、タイムコードを読み上げる。パネル変更後もドラッグの代替操作を提供する。

## 例外と復旧

モーダルを閉じたときに元の配置が消えていたら、同じパネルの一覧へ戻し、フォーカスの消失を防ぐ。

## 参照資料と確認項目

- [A042](https://helpx.adobe.com/premiere/desktop/get-started/set-up-accessibility-features/accessibility-overview.html)　画面配色、キーボード、読み上げの各経路で同じ編集対象を特定する。（公開手順）
- [A043](https://helpx.adobe.com/premiere/desktop/get-started/set-up-accessibility-features/screen-reader-screen-magnifier-and-operating-system-accessibility-support.html)　読み上げと拡大表示で対象の名前・値・選択状態と次の操作が分かる。（公開手順）
- [A044](https://helpx.adobe.com/premiere/desktop/get-started/set-up-accessibility-features/navigate-premiere-using-the-keyboard.html)　ポインターを使わずパネルを移り、再生、停止、選択解除まで完了する。（公開手順）
- [A057](https://helpx.adobe.com/premiere/desktop/get-started/use-touch-and-gesture-controls/use-thumbnail-controls-in-the-project-panel.html)　素材サムネイルを指でスクラブし、選択解除や誤ドラッグと区別する。（公開手順）
- [A058](https://helpx.adobe.com/premiere/desktop/get-started/use-touch-and-gesture-controls/learn-how-touch-and-gesture-actions-work-with-buttons.html)　同じボタンでタップ・長押し・ドラッグの結果を分け、取消後の状態を確認する。（公開手順）
- [A059](https://helpx.adobe.com/premiere/desktop/get-started/use-touch-and-gesture-controls/control-premiere-through-touch-and-gesture-in-microsoft-surface-pro-and-windows.html)　Windowsタッチ端末で拡大・スクロールを行い、クリップの配置を維持する。（公開手順）
