# 配置から原本への要件（ED-23）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

現在フレームの配置と素材の時刻を対応させ、原本で前後を確認する。

## 受入条件

タイムコード開始が1時間の素材と0開始のシーケンスで、両方が同じ絵を示す。

## 例外と復旧

選んだ行がギャップまたはオフラインの場合は理由を示し、素材モニターの前回の位置を別素材で上書きしない。

## 参照資料と確認項目

- [A089](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/compare-edits-to-clips-in-the-program-monitor.html)　比較モードで変更前後を水平・垂直に分割し、境界を動かして同一画素位置の差を見分けられるか試す。（公開手順）
- [A090](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/open-or-clear-a-clip-in-the-source-monitor.html)　Sourceでクリップを開いて表示を消去し、ビンの素材とタイムライン配置が残るか確かめる。（公開手順）
- [A091](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/navigate-clips-in-the-source-menu-in-the-source-monitor.html)　複数の素材をSourceに開き、ソースメニューから最初の素材を名前で再選択できるか試す。（公開手順）
- [A286](https://helpx.adobe.com/premiere/desktop/edit-projects/compare-edits-to-source-clips/compare-edits-to-clips-in-the-program-monitor.html)　Programのショット比較と同一フレームの変更前後比較を切り替え、左右を入れ替えても選んだ参照時刻を追えるか見る。（公開手順）
- [A287](https://helpx.adobe.com/premiere/desktop/edit-projects/compare-edits-to-source-clips/open-or-clear-a-clip-in-the-source-monitor.html)　Sourceだけを空にした後で同じクリップを開き直し、タイムラインの既存の配置が維持されているか確かめる。（公開手順）
- [A288](https://helpx.adobe.com/premiere/desktop/edit-projects/compare-edits-to-source-clips/navigate-clips-in-the-source-menu-in-the-source-monitor.html)　ソースメニューで繰り返し使うテイクへ戻り、同名の別素材を開いていないことをTCと原画で判断する。（公開手順）
- [A637](https://helpx.adobe.com/premiere/desktop/render-and-export/render-sequences-for-playback/match-a-frame-with-its-source.html)　トリム済みクリップの中間フレームでソースを開き、元ファイルの同じ撮影タイムコードが表示されるか照合する。（公開手順）
