# 素材の収集と保管の要件（IO-56）

[要件](requirements.md) ・ [設計](design.md) ・ [作業・試験](tasks.md) ・ [分野一覧](../README.md)

## 目的と範囲

選んだシーケンスが必要とする素材を収集または変換し、別の場所で復元する。

## 受入条件

元ストレージを切り離して別端末で開き、編集・書き出しを再現。AEリンク、プラグイン、フォント等の外部依存は別途記録。

## 例外と復旧

収集できない依存を明示して未解決一覧に残す。重複するファイル名は異なる内容を上書きしないよう割り当てる。

## 参照資料と確認項目

- [A107](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/copy-project.html)　案件のコピー側だけでカットを変更し、元の案件を開き直して変更が混ざらないか試す。（公開手順）
- [A108](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/consolidate-and-archive-projects.html)　使用素材を集約したアーカイブを別の場所で開き、採用カットと必要な音声がすべて再生できるか試す。（公開手順）
- [A109](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/move-project-to-another-computer.html)　異なるマウント名のPCへ案件を移し、素材場所を指定し直した後に同じ画と音が出るか照合する。（公開手順）
- [A110](https://helpx.adobe.com/premiere/desktop/organize-media/create-projects/delete-project.html)　試験用案件を削除し、別の案件も参照する原素材の存否を確認して削除範囲を区別する。（公開手順）
- [A173](https://helpx.adobe.com/premiere/desktop/organize-media/transfer-files/transfer-projects-from-one-computer-to-another.html)　別PCへ案件と必要ファイルを渡し、外部フォント・プラグイン・メディアなど実際に不足した依存を特定する。（公開手順）
- [A175](https://helpx.adobe.com/premiere/desktop/organize-media/transfer-files/copy-transcode-or-archive-project.html)　元尺コピーとトランスコードの両方式で素材を収集し、保存量、前後余白、再リンク後の区間を比較する。（公開手順）
