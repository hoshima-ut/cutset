# キーの割当と競合の要件（UI-04）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

全体、パネル、文字入力の各コンテキストについて現在の割当と衝突を検索できる。

## 受入条件

同じキーでも素材パネル、タイムライン、字幕入力中で対象が違う。色に加え作用先を文字で示し、競合と未割当を検索可能にする。文字入力中のDeleteでクリップを削除しない。

## 例外と復旧

同一コンテキストで衝突する割当は一方を解除する選択が確定するまで旧設定を維持する。

## 参照資料と確認項目

- [A045](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/about-keyboard-shortcuts.html)　全体キーとパネル専用キーが重なる場合にどちらが処理したかを確認する。（公開手順）
- [A046](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/default-keyboard-shortcuts.html)　工場出荷時の配列でWindowsとmacOSの操作結果を照合し、独自割当は別記する。（公開手順）
- [A047](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/customize-keyboard-shortcuts.html)　変更前と異なるキーを割り当て、競合表示・保存・適用結果を確認する。（公開手順）
- [A048](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/copy-keyboard-shortcuts-from-one-computer-to-another.html)　別端末に配列を持ち込み、配列名と代表的な3操作の一致を確かめる。（公開手順）
- [A049](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/assign-multiple-keyboard-shortcuts-to-a-command.html)　一つの操作に二つのキーを割り当て、両方から同じ履歴項目が作られる。（公開手順）
- [A050](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/find-keyboard-shortcuts.html)　操作名からキーを引く場合とキーから操作名を探す場合を別々に試す。（公開手順）
- [A051](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/remove-keyboard-shortcuts.html)　一方の割当だけを削除し、他のキーと操作自体は利用できることを確認する。（公開手順）
- [A052](https://helpx.adobe.com/premiere/desktop/get-started/keyboard-shortcuts/print-keyboard-shortcuts.html)　現在の配列を出力した一覧で、画面上の修飾キーと印刷した修飾キーを突き合わせる。（公開手順）
