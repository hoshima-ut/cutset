# 編集命令の共通化の要件（UX-01）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

マウス・キー・CLI・公式AI・第三者拡張から同じ対象を指定して同じ編集命令を実行する。

## 受入条件

マウス、キー、CLI、AI、外部プラグインで同じ配置を一フレーム詰める。各経路で配置ID、尺、影響範囲、Undo後の案件内容が一致する。

## 例外と復旧

意図した配置が消えた場合はどの入口でも同じ失敗理由となる。現在選択中の別配置に命令を振り替えない。

## 参照資料と確認項目

- [公開資料 1](https://github.com/storytold/filmcraft/blob/v0.20.1/README.md#architecture)
