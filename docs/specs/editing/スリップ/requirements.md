# スリップの要件（ED-29）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

配置位置と尺を固定し、参照する素材区間を前後に移す。

## 受入条件

素材の100–149番を103–152番にずらし、配置尺50フレームが保たれる。

## 例外と復旧

一方のリンク音声が素材端に達したら、その位置で全対象を止める。試聴中の取消では素材点を記録しない。

## 参照資料と確認項目

- [A236](https://helpx.adobe.com/premiere/desktop/edit-projects/trim-clips/perform-slip-edits.html)　スリップで素材In/Outだけを5フレームずらし、Timelineに置いた始点・終点・尺を維持できるか見る。（公開手順）
