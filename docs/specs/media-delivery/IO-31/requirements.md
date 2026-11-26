# IO-31 案件の移行 — 要件

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

保存版を検査し、変換前の版と未対応要素を保って別版へ移行する。

## 受入条件

26系の元案件を保持したまま別メジャーで開き、双方で再オープンできるファイルを区別。変換警告と欠落を記録。

## 例外と復旧

読込経路のない形式や将来版は理由を示して終了する。未知項目を捨てた状態で原本を自動保存しない。

## 参照資料と確認項目

- [A114](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/backward-compatibility-of-projects.html)　旧版のコピーを対象ビルドで開き、変換後ファイル名と元ファイルを区別して旧版でも元案件が開くか確認する。（公開手順）
- [A120](https://helpx.adobe.com/premiere/desktop/organize-media/import-files/import-a-premiere-elements-project.html)　公式が示すOS・版の組み合わせでElements案件のコピーを読み、移せたシーケンスと未対応項目を記録する。（公開手順）
- [A742](https://helpx.adobe.com/premiere/desktop/troubleshooting/limitations-and-known-issues/cannot-open-25-6-projects-in-25-x.html)　25.6で保存したコピーを旧版で開く試験を26系の互換結果から分ける。（25.6.0と他の25.xの旧版障害。26系一般仕様から除外）
