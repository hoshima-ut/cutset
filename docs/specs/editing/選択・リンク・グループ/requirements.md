# 選択・リンク・グループの要件（ED-18）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

同時選択、一緒に移動するグループ、同期対象の音声映像の関係を扱う。

## 受入条件

同じ素材を2回使い、選んだ配置だけを移動する。リンクした対とグループ外の素材を照合する。

## 例外と復旧

対象グループの一部がロックされている場合は、どの配置が移動できないか表示して確定を止める。

## 参照資料と確認項目

- [A210](https://helpx.adobe.com/premiere/desktop/edit-projects/intro-to-editing/apply-multi-transitions-across-audio-and-video-clips.html)　映像端を複数選択してトランジションを調整し、未選択カットと音声トランジションが意図せず変更されないか試す。（公開手順）
- [A258](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/copy-and-paste-clips.html)　リンクした映像・音声をコピーして指定位置へ貼り、素材In/Out、リンク関係と元配置の保持を照合する。（公開手順）
- [A259](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/different-ways-to-move-clips.html)　同じ選択クリップをドラッグと数フレームの移動コマンドで動かし、目標タイムコードで一致するか確かめる。（公開手順）
- [A260](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/rearrange-clips-on-the-timeline.html)　A・B・Cの中央を先頭へ並べ替え、途中に意図しない空白や他素材への上書きが入らないか再生する。（公開手順）
- [A270](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/select-clips.html)　重なった映像とリンク音声から任意の片側のみを選び、次の操作に含まれる配置を見分けられるか確認する。（26.5でSelection Follows Playheadのボタンを追加）
- [A271](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-sequence/group-clips.html)　三つの配置をグループ化して動かし、解除後は同じ一つの配置だけを独立に移動できるか試す。（公開手順）
