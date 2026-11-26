"""Check editable feature specifications and maintain their navigation pages."""

import re
from collections import defaultdict
from unicodedata import normalize
from urllib.parse import quote

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


PAGE_LABELS = {"requirements.md": "要件", "design.md": "設計", "tasks.md": "作業・試験"}


def feature_directory(spec, feature):
    category, key, title = feature["category"], feature["id"], feature["title"]
    if category not in CATEGORIES or not re.fullmatch(r"[A-Z]+-[0-9]+", key):
        raise ValueError(f"Invalid feature category or ID: {category}/{key}")
    # These names are also cloned on Windows and linked from GitHub Markdown.
    reserved = re.fullmatch(r"(CON|PRN|AUX|NUL|COM[1-9¹²³]|LPT[1-9¹²³])(\..*)?", title, re.I)
    if (not title or title != normalize("NFC", title) or title != title.strip()
            or title.endswith(".") or re.search(r'[<>:"/\\|?*\x00-\x1f]', title) or reserved
            or re.fullmatch(r"[A-Z]+-[0-9]+", title, re.I)):
        raise ValueError(f"{key}: invalid feature directory name {title!r}")
    return spec / category / title


def sections(path, feature):
    text = path.read_text(encoding="utf-8")
    wanted = f"# {feature['title']}の{PAGE_LABELS[path.name]}（{feature['id']}）"
    if text.partition("\n")[0] != wanted:
        raise ValueError(f"{path}: expected heading {wanted!r}")
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
    directories = set()
    for feature in features:
        key = feature["id"]
        directory = feature_directory(spec, feature)
        portable_name = directory.relative_to(spec).as_posix().casefold()
        if portable_name in directories:
            raise ValueError(f"{key}: duplicate feature directory {directory}")
        directories.add(portable_name)
        for name in PAGES:
            path = directory / name
            expected.add(path.relative_to(spec).as_posix())
            fields = sections(path, feature)
            if name == "requirements.md":
                summaries[key] = (fields["目的と範囲"], fields["受入条件"])
    # macOS may return decomposed names when enumerating a directory.
    listed = [normalize("NFC", p.relative_to(spec).as_posix())
              for name in PAGES for p in spec.glob(f"*/*/{name}")]
    actual = set(listed)
    if len(actual) != len(listed):
        raise ValueError("Found duplicate normalized feature document paths")
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
            title = row["title"]
            # Preserve Japanese in the Markdown source and escape URI delimiters and spaces.
            link = "".join(quote(char, safe="") if char.isascii() else char for char in title)
            table.append(f"| {title}（{key}） | [要件]({link}/requirements.md) | "
                         f"[設計]({link}/design.md) | [作業]({link}/tasks.md) | "
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
