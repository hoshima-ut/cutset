# UI-06 二つのモニター — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

素材とシーケンスを独立して試聴し、それぞれの再生位置と範囲を保持する。

## 受入条件

素材側は素材の時刻、完成側は配置後の時刻を表す。両方で同じ素材を異なる位置に開き、再生・I/Oがフォーカス側にだけ効くことを確認する。

## 例外と復旧

素材を閉じると素材側の操作を無効にし、残っている完成側への意図しない代替実行を防ぐ。

## 参照資料と確認項目

- [A082](https://helpx.adobe.com/premiere/desktop/get-started/source-and-program-monitor-adjustments/about-source-monitor-and-program-monitor.html)　Sourceで試した素材とProgramの完成画を別のフレームに置き、各モニターの時刻と表示対象を照合する。（既存モニター機能。映像と音声波形の同時表示は26.2）
