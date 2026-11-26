# トラック管理の要件（ED-11）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

種類、積層順、経路、表示、名前、ロックを個別に調整する。

## 受入条件

高さを変えても内容を維持。V2を非表示にすると下層が見え、A1の音量は変わらない。

## 例外と復旧

配置入りのトラック削除は失われる配置数を表示し、取消時はトラック順、名前、選択を復元する。

## 参照資料と確認項目

- [A261](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/add-tracks.html)　既存の音声トラックの間に新規トラックを加え、名前・種類と既配置クリップの所属が意図どおりか見る。（26.3で編集時の自動トラック作成を設定可能）
- [A262](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/delete-tracks.html)　空トラックと使用中トラックを別々に削除し、消える配置の範囲と残る素材ファイルを確認する。（公開手順）
- [A263](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/rename-tracks.html)　音楽用トラックを改名し、タイムラインのヘッダーと関連するミキサーの対応を追えるか確かめる。（公開手順）
- [A265](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/edit-track-appearance.html)　トラック高、サムネイル、波形表示を変え、狭い表示でも同じ編集点に吸着できるか試す。（26.2でトラック高変更の即時描画と音声チャンネルラベル表示を改善）
