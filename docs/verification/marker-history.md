# マーカーの追加と履歴

対象はED-55のマーカー追加とED-45のUndo/Redo。デモ案件にシーケンスマーカーを一つ追加し、同じセッションで取り消してやり直します。書き戻し先の指定は不要です。

```sh
mkdir -p target
./target/release/filmcraft-cli --demo run docs/verification/fixtures/marker-history.jsonl > target/marker-history.jsonl
python3 - <<'PY'
import json
from pathlib import Path

results = [json.loads(line) for line in Path("target/marker-history.jsonl").read_text().splitlines()]
assert len(results) == 7 and all(row["ok"] for row in results)
before, added, undone, redone = [results[i]["result"] for i in (0, 2, 4, 6)]
assert len(added["markers"]) == len(before["markers"]) + 1
assert before == undone and added == redone
PY
```

2026-11-26にmacOSのrelease CLIで実行し、全命令が成功しました。追加後にマーカーが一件増え、取り消し後のシーケンスは開始時、やり直し後は追加直後と一致しました。GUIでの操作と保存後の再開は別に確認します。[試験入力](fixtures/marker-history.jsonl)
