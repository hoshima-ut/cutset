#!/usr/bin/env python3
"""Check the public planning catalog against its references without network access."""

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "spec"
FEATURE_COUNTS = {
    "UI": 20, "IO": 56, "ED": 59, "FX": 21, "CO": 10, "GR": 8,
    "CC": 4, "AU": 18, "MN": 35, "UX": 14, "AI": 9, "WB": 5,
}


def rows(relative_path, key):
    data = json.loads((SPEC / relative_path).read_text(encoding="utf-8"))
    result = data[key]
    if not isinstance(result, list) or not all(isinstance(r, dict) for r in result):
        raise ValueError(f"{relative_path}: expected an array of records at {key}")
    return result


def unique_set(values, label):
    counts = Counter(values)
    duplicates = sorted(key for key, count in counts.items() if count > 1)
    if duplicates:
        raise ValueError(f"{label}: duplicate {duplicates[0]}")
    return set(counts)


def exact(actual, expected, label):
    if actual != expected:
        raise ValueError(
            f"{label}: missing {sorted(expected - actual)}, unexpected {sorted(actual - expected)}"
        )


def check_files(feature):
    paths = feature.get("baselineEvidence", [])
    if not isinstance(paths, list):
        raise ValueError(f"{feature['id']}: expected a list of evidence paths")
    if feature["baselineDisposition"] in {"reuse-partially", "extend"} and not paths:
        raise ValueError(f"{feature['id']}: missing baseline evidence")
    for link in paths + ([feature["details"]] if "details" in feature else []):
        path = Path(link)
        if path.is_absolute() or ".." in path.parts:
            raise ValueError(f"{feature['id']}: invalid project-relative path")
        target = (ROOT / path).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            raise ValueError(f"{feature['id']}: file missing or outside checkout: {link}")


def checked_reference(value, feature_ids, source):
    if value not in feature_ids:
        raise ValueError(f"{source}: unknown feature {value!r}")


CATEGORY_NAMES = {
    "workspace": "ワークスペース", "media-delivery": "素材管理と納品",
    "editing": "タイムライン編集", "effects": "合成と動き", "color": "カラー",
    "graphics": "グラフィック", "captions": "字幕", "audio": "音声",
    "commands": "メニューと文脈依存の操作", "workflow": "編集者のワークフロー",
    "ai-plugin": "AIと拡張", "browser": "ブラウザ",
}

DISPOSITIONS = {
    "reuse-partially": "上流部品を再利用", "extend": "上流部品を拡張",
    "new-design": "新規設計", "verify": "上流対応を要調査",
}


def feature_overview(features):
    lines = [
        "# Cutsetの機能仕様", "",
        "[機械可読の正本](../catalog.json)にある各項目の操作と受入条件。"
        "記載する状態は開発計画で、上流部品の存在だけでは編集者向けの受入合格にならない。", "",
        "各領域の[操作・アクセシビリティ・AIの共通条件](interaction.md)、"
        "[180のキー操作意図](keyboard.json)、[効果・音響処理・形式別の受入](rendering.md)、"
        "[12件の横断試験](journeys.json)も同じ仕様に含む。"
        "領域をまたぐ入力の扱いは[モデル接続](../model-connections.md)を参照。", "",
        "[資料台帳](../sources.json)は公開記事ごとの版注記と独自の照合例を持つ。"
        "27系・ベータ・旧版・障害診断・外部サービスに関する項目は比較用の根拠である。"
        "特定ビルドの全画面・非公開仕様を観測したという意味は持たない。", "",
        "操作IDの既存実装は[継承コマンド](../native-commands.tsv)から引ける。"
        "各機能の上流実装候補と出典URLは正本の同じIDに記録する。", "",
        "更新時は正本を編集して `python3 tools/check_catalog_links.py --write-overview` で本ページを再生成する。", "",
    ]
    for category, name in CATEGORY_NAMES.items():
        lines.append(f"- [{name}](#{category})")
    for category, name in CATEGORY_NAMES.items():
        lines.extend(["", f'<a id="{category}"></a>', "", f"## {name}", ""])
        for item in features:
            if item["category"] != category:
                continue
            lines.extend([
                f"### {item['id']} {item['title']}", "",
                item["scope"], "",
                f"**受入**　{item['acceptance']}", "",
                f"**実装方針**　{DISPOSITIONS[item['baselineDisposition']]} ・ [目標 {item['milestone']}](../milestones.md)", "",
            ])
    return "\n".join(lines).rstrip() + "\n"


def check_native(ids, commands_json):
    with (SPEC / "native-commands.tsv").open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if not {"command", "feature", "registrySource", "label", "menu", "defaultShortcut", "params"} <= set(reader.fieldnames or []):
            raise ValueError("native-commands.tsv: required header missing")
        contract_by_command = {}
        for line, row in enumerate(reader, start=2):
            label = f"native-commands.tsv line {line}"
            checked_reference(row["feature"], ids, label)
            check_files({
                "id": label, "baselineDisposition": "extend",
                "baselineEvidence": [row["registrySource"]],
            })
            if not row["command"] or any(c.isspace() for c in row["command"]):
                raise ValueError(f"{label}: invalid command ID")
            name = row["command"]
            if name in contract_by_command:
                raise ValueError(f"{label}: duplicate command ID {name}")
            contract_by_command[name] = (row["label"], row["menu"], row["defaultShortcut"], row["params"])
    command_ids = set(contract_by_command)
    if not command_ids:
        raise ValueError("native-commands.tsv: no commands")
    canonical = ("\n".join(sorted(command_ids)) + "\n").encode("utf-8")
    if hashlib.sha256(canonical).hexdigest() != (
        SPEC / "native-command-set.sha256"
    ).read_text(encoding="utf-8").strip():
        raise ValueError("native command IDs differ from the pinned registry digest")
    if commands_json is not None:
        registry = json.loads(commands_json.read_text(encoding="utf-8"))
        if not isinstance(registry, list):
            raise ValueError("--commands-json: expected filmcraft-cli commands --json array")
        live = unique_set((cmd["id"] for cmd in registry), "live command registry")
        exact(command_ids, live, "live command registry")
        for cmd in registry:
            observed = (cmd["label"], " > ".join(cmd["menu"]), cmd["defaultShortcut"] or "", cmd["params"])
            if observed != contract_by_command[cmd["id"]]:
                raise ValueError(f"live command metadata differs for {cmd['id']}")
    return len(command_ids)


def verify(commands_json, write_overview):
    features = rows("catalog.json", "features")
    ids = unique_set((row["id"] for row in features), "catalog")
    expected = {
        f"{prefix}-{i:02d}" for prefix, count in FEATURE_COUNTS.items()
        for i in range(1, count + 1)
    }
    exact(ids, expected, "catalog IDs")
    for item in features:
        if item.get("milestone") not in {"M1", "M2", "M3", "M4", "M5", "M6"}:
            raise ValueError(f"{item['id']}: unknown milestone")
        check_files(item)
        for key in ("title", "scope", "acceptance", "category", "status"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError(f"{item['id']}: missing {key}")

    articles = rows("sources.json", "articles")
    article_ids = unique_set((a["id"] for a in articles), "source IDs")
    exact(article_ids, {f"A{i:03d}" for i in range(1, 814)}, "source IDs")
    unique_set((a["url"] for a in articles), "article URLs")
    for article in articles:
        checked_reference(article["feature"], ids, article["id"])
        url = urlsplit(article["url"])
        if url.scheme != "https" or url.netloc != "helpx.adobe.com" or not url.path:
            raise ValueError(f"{article['id']}: invalid official URL")
        if not article["probe"].strip() or not article["referenceScope"].strip():
            raise ValueError(f"{article['id']}: missing version scope or probe")

    journeys = rows("features/journeys.json", "journeys")
    journey_ids = unique_set((row["id"] for row in journeys), "journeys")
    exact(journey_ids, {f"QA-{i:02d}" for i in range(1, 13)}, "journey IDs")
    for journey in journeys:
        if not journey["features"] or not journey["setup"].strip() or not journey["expected"].strip():
            raise ValueError(f"{journey['id']}: incomplete journey")
        for feature_id in journey["features"]:
            checked_reference(feature_id, ids, journey["id"])

    groups = rows("features/keyboard.json", "groups")
    intents = []
    for group in groups:
        checked_reference(group["feature"], ids, group["context"])
        intents.extend((group["context"], action) for action in group["intents"])
    if len(unique_set(intents, "keyboard intents")) != 180:
        raise ValueError("expected 180 contextual keyboard intents")

    native_count = check_native(ids, commands_json)
    overview = feature_overview(features)
    overview_file = SPEC / "features/README.md"
    if write_overview:
        overview_file.write_text(overview, encoding="utf-8")
    elif overview_file.read_text(encoding="utf-8") != overview:
        raise ValueError("feature overview stale: use --write-overview")

    return {"features": len(ids), "sources": len(articles), "journeys": len(journeys),
            "keyboard_intents": len(intents), "native_commands": native_count}



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commands-json", type=Path, help="filmcraft-cli commands --json output")
    parser.add_argument("--write-overview", action="store_true", help="refresh the catalog Markdown")
    arguments = parser.parse_args()
    try:
        print(json.dumps(verify(arguments.commands_json, arguments.write_overview)))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Catalog link check failed: {error}", file=sys.stderr)
        sys.exit(1)
