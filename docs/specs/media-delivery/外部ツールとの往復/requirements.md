# 外部ツールとの往復の要件（IO-38）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

音声・静止画・合成素材を外部ツールに渡し、戻り素材の時刻・版を照合する。

## 受入条件

生成した音声ステムを加工して取り込むと、元の開始サンプルと行き先が一致する。リンク先を移動した場合は旧版を保持し、再接続先を選べる。

## 例外と復旧

外部作業中に元配置が移動したら、戻り先を確認する。尺が異なる場合は差を示して旧配置を維持する。

## 参照資料と確認項目

- [A163](https://helpx.adobe.com/premiere/desktop/organize-media/apply-labeling/share-markers-with-after-effects.html)　マーカー付きの参照素材をAfter Effectsとの対応経路に渡し、名称・時刻・範囲のうち残る項目を記録する。（公開手順）
- [A523](https://helpx.adobe.com/premiere/desktop/add-audio-effects/advanced-audio-techniques/remix-audio-in-audition-to-match-video-duration.html)　検証用の曲をAudition側で指定映像尺へリミックスし、Premiereへ戻した長さとつなぎ目を確認する。（公開手順）
- [A601](https://helpx.adobe.com/premiere/desktop/correct-color/set-up-color-management/premiere-after-effects-color-management-compatibility.html)　Dynamic Linkを通す前後に同じ色見本を置き、PremiereとAfter Effectsの解釈を突き合わせる。（公開手順）
- [A791](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/transfer-of-information-from-premiere-to-audition.html)　音量変化とフェードを付けてAuditionへ送り、渡る情報とレンダーされた調整を別々に調べる。（公開手順）
- [A792](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/edit-premiere-sequences-in-audition.html)　複数トラックの選択シーケンスをAuditionで開き、対象区間・個別クリップ・開始時刻の対応を確認する。（公開手順）
- [A793](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/edit-premiere-audio-clips-in-audition.html)　単一クリップをAuditionに送って波形を修正し、生成されたWAVと元の録音ファイルを比較する。（公開手順）
- [A794](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/import-after-effects-compositions.html)　複数コンポを持つAEPから一つを指定して取り込み、同名の別コンポを誤って開かないか確認する。（公開手順）
- [A795](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/replace-clips-with-a-dynamically-linked-after-effects-composition.html)　タイムラインの連続2クリップをAEコンポに置き換え、置換区間の先頭と末尾が元と同じか測る。（公開手順）
- [A796](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/delete-dynamically-linked-compositions-or-clips.html)　リンクした配置を一つ削除し、コンポジション自体と別の配置が引き続き使えるか確認する。（公開手順）
- [A797](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/make-a-dynamically-linked-composition-offline.html)　AEコンポをオフラインにし、レンダーが利用できない部分と保持された配置情報を見分ける。（公開手順）
- [A798](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/relink-a-dynamically-linked-composition.html)　移動したAEPを再指定してリンクし、同一プロジェクト内の目的コンポが表示されるか照合する。（公開手順）
- [A799](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/copy-clips-from-premiere-to-after-effects.html)　Premiereの複数クリップをAEへコピーし、開始位置・トリム・対応する効果がどのレイヤーに渡るか調べる。（公開手順）
- [A800](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/copy-from-after-effects-to-premiere.html)　AEの複数レイヤーをPremiereへ貼り、重なり順と未変換の機能をタイムラインで照合する。（公開手順）
- [A802](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/create-a-photoshop-file-in-a-project.html)　編集中シーケンスからPhotoshopファイルを新規作成し、寸法・ピクセル比と保存場所を調べる。（公開手順）
- [A803](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/edit-still-images-in-premiere-using-photoshop.html)　配置済み静止画をPhotoshopで更新し、案件を開いたまま変更が見えるかと編集点を維持できるか確認する。（公開手順）
- [A804](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/share-assets-between-after-effects-and-premiere-using-dynamic-link.html)　新規レンダーファイルを書き出さずにAEの変更をPremiereで確認し、対応版の組み合わせを控える。（公開手順）
- [A805](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/replace-clips-with-a-dynamically-linked-after-effects-composition0.html)　別トラックに重なる素材をAEコンポに置き換え、置換対象外の音声と上位トラックが残るか確かめる。（公開手順）
- [A806](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/create-a-dynamically-linked-composition.html)　Premiere側から空のリンクコンポを作り、AEで最初の図形を追加して同じ時点へ戻れるか確認する。（公開手順）
- [A807](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/import-an-after-effects-composition.html)　既存AEPのリンクを別のPremiere案件にも読み込み、元での調整が両方に届くか観察する。（公開手順）
- [A808](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/delete-a-dynamicaly-linked-composition-or-clip.html)　リンク済みのクリップを案件パネルから取り除き、参照中のシーケンスにどのような影響が出るか試験用コピーで調べる。（公開手順）
- [A809](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/modify-a-dynamically-linked-composition-in-after-effects.html)　AE側で色と尺を変え、戻ったPremiereの表示と既存カットの範囲をそれぞれ確認する。（公開手順）
- [A810](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/make-a-dynamically-linked-composition-offline0.html)　リンクを意図的にオフライン化し、原本AEPが残った状態と実際に移動した状態とを区別する。（公開手順）
- [A811](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/relink-a-dynamically-linked-composition0.html)　異なるフォルダーに同名AEPを用意し、再接続時に正しいコンポの識別用フレームが出るか調べる。（公開手順）
- [A812](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/how-premiere-works-with-audition-for-audio-editing.html)　Audition連携のクリップ単位とシーケンス単位を比べ、戻す成果物と編集可能な音声の範囲を記録する。（公開手順）
- [A813](https://helpx.adobe.com/premiere/desktop/use-premiere-with-other-apps/working-with-other-adobe-applications/work-with-photoshop-and-premiere.html)　PhotoshopとPremiereで同じタイトル素材を往復し、アルファ、レイヤーサイズ、色の変化を確認する。（公開手順）
