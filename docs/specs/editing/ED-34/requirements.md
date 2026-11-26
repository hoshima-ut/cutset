# ED-34 速度の時間変化 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

位置と素材時刻の対応を速度キーフレームで変え、補間の種類を指定する。

## 受入条件

動体とカット境界を含む素材で速度曲線、保持区間、補間由来の破綻を試聴比較する。

## 例外と復旧

重複したキー時刻や素材外に出る曲線を確定しない。補間できない区間は実際に選択した代替方式を明示する。

## 参照資料と確認項目

- [A154](https://helpx.adobe.com/premiere/desktop/organize-media/file-organization/freeze-a-frame-for-a-portion-of-a-clip-using-time-remapping.html)　動作中の途中5フレームだけを静止させ、前後では動きが続くこととホールド時の元フレームを照合する。（公開手順）
- [A247](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/change-clip-speed-and-duration-using-time-remapping.html)　速度線に二つのキーを置いて中間だけを加速し、ベジェ調整による滑らかさと変更後の終了時刻を比較する。（公開手順）
- [A248](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/apply-time-interpolation-methods-to-adjust-clip-speed.html)　同じ減速素材でサンプリング、ブレンド、光学フローを切り替え、動体の輪郭とカット境界の補間結果を確認する。（公開手順）
- [A249](https://helpx.adobe.com/premiere/desktop/edit-projects/change-clip-speed/remove-time-remapping-from-a-clip.html)　速度変化のある配置からTime Remappingを消去し、元の再生速度と他の効果パラメータを照合する。（公開手順）
