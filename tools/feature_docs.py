"""Check editable feature specifications and maintain their navigation pages."""

import re
from collections import defaultdict
from pathlib import Path

CATEGORIES = {
    "workspace": "ワークスペース", "media-delivery": "素材管理と納品",
    "editing": "タイムライン編集", "effects": "エフェクト", "color": "カラー",
    "graphics": "グラフィック", "captions": "字幕", "audio": "音声",
    "commands": "メニューと文脈操作", "workflow": "編集ワークフロー",
    "ai-plugin": "AIと拡張", "browser": "ブラウザ",
}
POLICIES = {
    "reuse-partially": "既存部品を利用", "extend": "既存部品を拡張",
    "new-design": "新規設計", "verify": "上流対応を要確認",
}
PAGES = {
    "requirements.md": ("目的と範囲", "受入条件", "例外と復旧"),
    "design.md": ("操作と状態遷移", "データと処理境界", "既存実装との対応"),
    "tasks.md": ("実装と検証", "具体的な試験", "既存テストとの対応"),
}


def sections(path, feature_id):
    text = path.read_text(encoding="utf-8")
    if not text.startswith(f"# {feature_id} "):
        raise ValueError(f"{path}: incorrect feature ID")
    pieces = re.split(r"^## (.+)\n", text, flags=re.MULTILINE)
    result = {}
    for name, body in zip(pieces[1::2], pieces[2::2]):
        if name in result or not body.strip():
            raise ValueError(f"{path}: empty or duplicate section {name}")
        result[name] = body.strip()
    for name in PAGES[path.name]:
        if not result.get(name):
            raise ValueError(f"{path}: missing {name}")
    return result


def check_pages(spec, features):
    """requirements.md owns scope and acceptance. Return the projection for the catalog."""
    expected = set()
    summaries = {}
    for feature in features:
        category, key = feature["category"], feature["id"]
        if category not in CATEGORIES or not re.fullmatch(r"[A-Z]+-[0-9]+", key):
            raise ValueError(f"Invalid feature directory: {category}/{key}")
        directory = spec / category / key
        for name in PAGES:
            path = directory / name
            expected.add(path)
            fields = sections(path, key)
            if name == "requirements.md":
                summaries[key] = (fields["目的と範囲"], fields["受入条件"])
    actual = {p for name in PAGES for p in spec.glob(f"*/*/{name}")}
    if actual != expected:
        raise ValueError(f"Unexpected feature documents: {sorted(actual - expected)}")
    return summaries


def indexes(spec, features):
    by_category = defaultdict(list)
    for row in features:
        by_category[row["category"]].append(row)
    output = {}
    top = ["# 機能索引", "", "機能を選ぶと要件・設計・作業の3文書を開けます。"
           "実装状況の根拠は各設計書、実行した試験と残る確認は作業表に記載します。"
           "[検証範囲](../verification/coverage.md) ・ [仕様の更新方法](README.md)", "",
           "| 分野 | 機能数 |", "| --- | ---: |"]
    for category, title in CATEGORIES.items():
        rows = by_category[category]
        top.append(f"| [{title}]({category}/README.md) | {len(rows)} |")
        table = [f"# {title}", "", "[全分野](../index.md) ・ [共通の操作条件](../shared/interaction.md)", "",
                 "| 機能 | 要件 | 設計 | 作業・試験 | 方針 | 目標 |",
                 "| --- | --- | --- | --- | --- | --- |"]
        for row in rows:
            key = row["id"]
            table.append(f"| {key} {row['title']} | [要件]({key}/requirements.md) | "
                         f"[設計]({key}/design.md) | [作業]({key}/tasks.md) | "
                         f"{POLICIES[row['baselineDisposition']]} | {row['milestone']} |")
        output[spec / category / "README.md"] = "\n".join(table) + "\n"
    output[spec / "index.md"] = "\n".join(top) + "\n"
    return output


def sync_projection(spec, features, write=False):
    summaries = check_pages(spec, features)
    for row in features:
        scope, acceptance = summaries[row["id"]]
        if write:
            row.update(scope=scope, acceptance=acceptance)
        elif (row["scope"], row["acceptance"]) != (scope, acceptance):
            raise ValueError(f"{row['id']}: requirements changed; run --write-overview")


def sync(spec, features, write):
    sync_projection(spec, features, write)
    for path, text in indexes(spec, features).items():
        if write:
            path.write_text(text, encoding="utf-8")
        elif path.read_text(encoding="utf-8") != text:
            raise ValueError(f"Stale index {path}: run --write-overview")
