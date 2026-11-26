# ED-39 没入型の編集 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

球面投影・左右眼と空間音声の配置を編集し、試聴の向きと作品の向きを分ける。

## 受入条件

左右に音源のあるパノラマで視点を回し、表示用の向き変更と書き出しメタデータを別々に確認。

## 例外と復旧

投影方式、眼の配置、音声形式が不足している場合は不足項目を示し、未確認の空間メタデータで納品しない。

## 参照資料と確認項目

- [A291](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/vr-editing-in-premiere-pro.html)　360度テスト素材を読み込んで全天球ビューと平面表示を切り替え、正面の目印を同じ時刻で特定できるか試す。（公開手順）
- [A292](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/vr-auto-detection.html)　VR属性あり・なしの二つの素材を読み、自動検出された投影とステレオ設定をメタデータと比較する。（公開手順）
- [A293](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/interpret-vr-footage.html)　左右眼構成を手動指定し直し、平面で横並びだった試験映像が正しい視差で表示されるか確かめる。（公開手順）
- [A294](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/assign-vr-properties-to-sequences.html)　VR設定付きシーケンスを作って投影・レイアウトを保存し、再度開いて指定値を読み戻せるか見る。（公開手順）
- [A295](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/360-degree-panning.html)　360度表示を水平に一周させ、つなぎ目を越えて同じ目印に連続して戻るか確認する。（公開手順）
- [A296](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/vr-assignments.html)　同じ素材でVR属性を割り当てた場合と未指定の場合を比べ、ビューアーの有効化と投影方式の初期値を確認する。（公開手順）
- [A297](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/hide-vr-video-view-controls.html)　VRビューのコントロールだけを隠して、球面表示と現在の向きを保ったまま再表示できるか試す。（公開手順）
- [A300](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/assembling-ambisonics-audio.html)　方向別テスト信号をアンビソニックスとして組み、必要なチャンネル数・配置順と音場の対応を照合する。（公開手順）
- [A301](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/monitor-ambisonics-audio.html)　VRビューで向きを変えながら方向付き音源を再生し、基準方向に対して左右の聞こえ方が変わるか確認する。（公開手順）
- [A302](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/restage-correctly-aligned-video-and-audio.html)　舞台の向きを変えた360度映像と音場を同じ角度で再配置し、見える楽器と聞こえる方向が一致するか確かめる。（公開手順）
- [A303](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/publish-vr-videos.html)　VR属性を指定して書き出し、対応プレーヤーが球面映像とステレオ構成を正しく認識するか確認する。（公開手順）
- [A304](https://helpx.adobe.com/premiere/desktop/edit-projects/edit-vr-content/vr-editing-in-premiere.html)　全天球素材を読み込みから試聴、方向調整、引き渡しまで通し、再読込時にも投影属性を識別できるか確かめる。（公開手順）
