# 選択依存のインスペクターの要件（UI-07）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

単一・複数・ロック・選択なしの各状態で変更可能な共通属性を示す。

## 受入条件

無選択、同種複数選択、異種選択、ロックの4状態で表示する操作が変わる。混在した値を一つに見せず、変更対象数を示す。素材全体と一配置の効果を別表示する。

## 例外と復旧

確定時に対象が削除・ロックされていれば変更を止め、対象群を更新して再確認を求める。

## 参照資料と確認項目

- [A070](https://helpx.adobe.com/premiere/desktop/get-started/tour-the-workspace/clip-details-in-the-info-panel.html)　タイムライン上の選択を変え、Infoの素材、時間、選択件数が連動する。（公開手順）
- [A217](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/edit-video-using-the-properties-panel.html)　複数の配置を選んでPropertiesから共通の位置を変え、選ばなかった配置と素材自体の属性を維持できるか確かめる。（既存パネル。音声・映像効果とマスクをPropertiesにカード表示するUIは27.0）
- [A332](https://helpx.adobe.com/premiere/desktop/add-text-images/stylize-text/about-properties-panel.html)　字幕、音声、図形を順に選択し、表示される設定と編集結果が選択対象に対応するか確認する。（既存パネル。音声・映像効果とマスクをPropertiesにカード表示するUIは27.0）
