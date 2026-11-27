#!/usr/bin/env python3
"""Trace a Cutset contract through its local verification. All CLI output is JSON."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from feature_docs import sync_projection

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {
    ("python3", "tools/test_cutset_harness.py"),
    ("python3", "tools/test_cutset_trial.py"),
}
ID = re.compile(r"[A-Z][A-Z0-9-]*\Z")
MAX_STEPS = 10
# A Rust check names a workspace package, one integration test binary and a test-name filter; the
# harness builds the command itself, so the graph cannot smuggle flags or shell text into it.
CARGO_FIELDS = {"package", "test", "filter"}
CARGO_NAME = re.compile(r"[a-z][a-z0-9_-]*\Z")
CARGO_FILTER = re.compile(r"[A-Za-z0-9_:]+\Z")
CARGO_RESULT = re.compile(r"^test result: (ok|FAILED)\. (\d+) passed; (\d+) failed", re.MULTILINE)
TIMEOUT = {"python": 60, "cargo": 1800}


def demand(condition, message):
    if not condition:
        raise ValueError(message)


def keyed(rows, label):
    result = {}
    demand(isinstance(rows, list), f"{label} must be an array")
    for row in rows:
        demand(isinstance(row, dict), f"invalid {label} row")
        ident = row.get("id")
        demand(isinstance(ident, str) and ID.fullmatch(ident), f"invalid {label} id")
        demand(ident not in result, f"duplicate {label} {ident}")
        result[ident] = row
    return result


def refs(row, key, targets, required=False):
    values = row.get(key)
    demand(isinstance(values, list) and all(isinstance(x, str) for x in values),
           f"{row['id']}: invalid {key}")
    demand(len(values) == len(set(values)) and (values or not required),
           f"{row['id']}: duplicate or missing {key}")
    for target in values:
        demand(target in targets, f"{row['id']}: unknown {key} {target}")
    return values


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def workspace_packages(root):
    """Package names of the workspace members under crates/ and apps/."""
    names = set()
    for manifest in [*root.glob("crates/*/Cargo.toml"), *root.glob("apps/*/Cargo.toml")]:
        found = re.search(r'^name\s*=\s*"([^"]+)"', manifest.read_text(encoding="utf-8"), re.MULTILINE)
        if found:
            names.add(found[1])
    return names


def command(check):
    """The argv a check runs; Python checks are listed in ALLOWED, Rust checks are built here."""
    cargo = check.get("cargo")
    if cargo is None:
        return check["argv"]
    return ["cargo", "test", "--locked", "-p", cargo["package"], "--test", cargo["test"], "--", cargo["filter"]]


def validate_check(key, check, packages):
    cargo = check.get("cargo")
    if cargo is None:
        argv = check.get("argv")
        demand(isinstance(argv, list) and all(isinstance(arg, str) for arg in argv)
               and tuple(argv) in ALLOWED, f"{key}: unsupported command")
        return
    demand("argv" not in check and isinstance(cargo, dict) and set(cargo) == CARGO_FIELDS
           and all(isinstance(cargo[f], str) for f in CARGO_FIELDS), f"{key}: invalid cargo check")
    demand(CARGO_NAME.fullmatch(cargo["package"]) and cargo["package"] in packages,
           f"{key}: unknown cargo package {cargo['package']}")
    demand(CARGO_NAME.fullmatch(cargo["test"]) and CARGO_FILTER.fullmatch(cargo["filter"]),
           f"{key}: invalid cargo test or filter")


def cargo_tests(output):
    """Tests passed across every test binary, or 0 when any binary failed or none ran."""
    results = CARGO_RESULT.findall(output)
    if not results or any(state != "ok" or int(failed) for state, _, failed in results):
        return 0
    return sum(int(passed) for _, passed, _ in results)


class Graph:
    def __init__(self, catalog, manifest, packages=frozenset()):
        demand(isinstance(catalog, dict) and isinstance(manifest, dict), "expected JSON objects")
        self.features = keyed(catalog.get("features"), "feature")
        self.tasks = keyed(manifest.get("tasks"), "task")
        self.criteria = keyed(manifest.get("acceptance"), "acceptance")
        self.checks = keyed(manifest.get("checks"), "check")
        demand(bool(self.features), "empty feature catalog")
        self.nodes = {}
        self.edges = []
        for key, feature in self.features.items():
            self.node("feature", feature, "title")
            task, criterion = f"BUILD-{key}", f"AC-{key}"
            row = self.tasks.setdefault(task, dict(id=task, title=feature["title"], specs=[key],
                                                    requires=[], acceptance=[criterion]))
            demand(isinstance(row.get("specs"), list) and key in row["specs"]
                   and isinstance(row.get("acceptance"), list) and criterion in row["acceptance"],
                   f"{task} must retain its feature contract")
            entry = self.criteria.setdefault(criterion, dict(id=criterion, checks=[]))
            demand("description" not in entry or entry["description"] == feature.get("acceptance"),
                   f"{criterion} must use its catalog acceptance")
            self.criteria[criterion] = dict(entry, description=feature.get("acceptance"))
        used_criteria, used_checks = set(), set()
        for key, task in self.tasks.items():
            self.node("task", task, "title")
            for feature in refs(task, "specs", self.features):
                self.edge("feature", feature, "scopes", "task", key)
            for dependency in refs(task, "requires", self.tasks):
                self.edge("task", dependency, "precedes", "task", key)
            for criterion in refs(task, "acceptance", self.criteria, required=True):
                self.edge("task", key, "requires_acceptance", "acceptance", criterion)
                used_criteria.add(criterion)
        for key, criterion in self.criteria.items():
            self.node("acceptance", criterion, "description")
            for check in refs(criterion, "checks", self.checks):
                self.edge("acceptance", key, "verified_by", "check", check)
                used_checks.add(check)
        demand(used_criteria == set(self.criteria), "orphan acceptance criterion")
        demand(used_checks == set(self.checks), "orphan check")
        for key, check in self.checks.items():
            validate_check(key, check, packages)
            self.nodes["check:" + key] = dict(check, type="check", argv=command(check))
        self.ensure_acyclic()

    def node(self, kind, row, text):
        value = row.get(text)
        demand(isinstance(value, str) and value.strip(), f"{row['id']}: invalid {text}")
        self.nodes[f"{kind}:{row['id']}"] = dict(row, type=kind)

    def edge(self, left_kind, left, relation, right_kind, right):
        self.edges.append({"from": f"{left_kind}:{left}", "relation": relation, "to": f"{right_kind}:{right}"})

    def ensure_acyclic(self):
        waiting = {key: set(task["requires"]) for key, task in self.tasks.items()}
        while waiting:
            frontier = {key for key, dependencies in waiting.items() if not dependencies}
            demand(frontier, "cycle in task dependencies")
            waiting = {key: deps - frontier for key, deps in waiting.items() if key not in frontier}

    def checks_for(self, task):
        groups = [self.criteria[key]["checks"] for key in self.tasks[task]["acceptance"]]
        if not all(groups):
            return []
        return sorted({key for group in groups for key in group})

    def query(self, ident, transitive=False):
        if ident not in self.nodes:
            matches = [name for name in self.nodes if name.partition(":")[2] == ident]
            demand(len(matches) == 1, f"unknown or ambiguous node {ident}")
            ident = matches[0]
        if not transitive:
            return {"node": self.nodes[ident], "edges": [
                edge for edge in self.edges if ident in (edge["from"], edge["to"])]}
        seen, frontier = {ident}, {ident}
        while frontier:
            frontier = {e["to"] for e in self.edges if e["from"] in frontier} - seen
            seen.update(frontier)
        return {"origin": ident, "reachable": sorted(seen - {ident})}


def git(root, *args):
    return subprocess.check_output(["git", *args], cwd=root, text=True, stderr=subprocess.DEVNULL).strip()


def snapshot(root):
    return {
        "revision": git(root, "rev-parse", "HEAD"),
        "tree": git(root, "rev-parse", "HEAD^{tree}"),
        "clean": not git(root, "status", "--porcelain=v1", "--untracked-files=normal",
                         "--ignore-submodules=none"),
    }


def python_tests(output):
    summary = re.search(r"^Ran (\d+) tests? in [^\n]+\s+OK\s*\Z", output, re.MULTILINE)
    return int(summary[1]) if summary else 0


def run_check(root, check):
    argv = command(check)
    kind = "cargo" if "cargo" in check else "python"
    runnable = argv if kind == "cargo" else [sys.executable, "-E", "-s", "-B", argv[1]]
    try:
        proc = subprocess.run(runnable, cwd=root, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                              timeout=TIMEOUT[kind])
    except subprocess.TimeoutExpired:
        return dict(id=check["id"], argv=argv, exit_code=124, tests=0, passed=False)
    output = proc.stdout.decode("utf-8", errors="replace")
    count = (cargo_tests if kind == "cargo" else python_tests)(output)
    return dict(id=check["id"], argv=argv, exit_code=proc.returncode,
                tests=count, passed=proc.returncode == 0 and count > 0)


class Session:
    def __init__(self, root):
        self.root = root
        self.state = snapshot(root)
        catalog, manifest = (read(root / "docs/specs/data" / name) for name in ("catalog.json", "graph.json"))
        self.graph = Graph(catalog, manifest, workspace_packages(root))
        sync_projection(root / "docs/specs", list(self.graph.features.values()))
        data = json.dumps([catalog, manifest], sort_keys=True).encode()
        self.digest = hashlib.sha256(data).hexdigest()
        self.directory = root / "target" / "cutset-harness" / self.state["revision"]

    def receipt(self, task):
        if not self.state["clean"]:
            return None
        path = self.directory / (task + ".json")
        if path.resolve() != path or not path.is_file():
            return None
        try:
            row = read(path)
            checks = self.graph.checks_for(task)
            if not isinstance(row, dict) or not checks or any((
                row.get("snapshot") != self.state, row.get("task") != task,
                row.get("contract_sha256") != self.digest,
            )):
                return None
            results = row.get("results")
            if not isinstance(results, list) or len(results) != len(checks):
                return None
            for key, result in zip(checks, results):
                if (not isinstance(result, dict) or result.get("id") != key
                    or result.get("argv") != command(self.graph.checks[key])
                    or result.get("exit_code") != 0 or result.get("passed") is not True
                    or type(result.get("tests")) is not int or result["tests"] <= 0):
                    return None
            return row
        except (ValueError, OSError):
            return None

    def prerequisites_pass(self, task):
        visited = set()
        pending = list(self.graph.tasks[task]["requires"])
        while pending:
            key = pending.pop()
            if key not in visited:
                if not self.receipt(key):
                    return False
                visited.add(key)
                pending.extend(self.graph.tasks[key]["requires"])
        return True

    def status(self, task):
        if not self.graph.checks_for(task):
            return "planned"
        if not self.prerequisites_pass(task):
            return "blocked"
        if self.receipt(task):
            return "review_pending"
        return "ready"

    def execute(self, task):
        demand(task in self.graph.tasks, f"unknown task {task}")
        demand(self.state["clean"] and snapshot(self.root) == self.state,
               "verification needs a clean, stable commit; run the test script directly during editing")
        demand(self.status(task) in ("ready", "review_pending"), f"{task} is {self.status(task)}")
        demand(self.directory.resolve() == self.directory, "evidence directory is a symlink")
        self.directory.mkdir(parents=True, exist_ok=True)
        lock = self.directory / ".running"
        try:
            lock.mkdir()
        except FileExistsError as exc:
            raise ValueError("another check owns the revision lock") from exc
        try:
            demand(snapshot(self.root) == self.state and self.status(task) in ("ready", "review_pending"),
                   "inputs or prerequisites changed before verification")
            row = dict(task=task, snapshot=self.state, contract_sha256=self.digest, results=[])
            self.write_receipt(task, row)
            for key in self.graph.checks_for(task):
                row["results"].append(run_check(self.root, self.graph.checks[key]))
            demand(snapshot(self.root) == self.state, "worktree changed during checks; evidence discarded")
            self.write_receipt(task, row)
            return row
        finally:
            lock.rmdir()

    def write_receipt(self, task, row):
        with tempfile.NamedTemporaryFile(dir=self.directory, mode="w", delete=False) as temporary:
            json.dump(row, temporary)
        os.replace(temporary.name, self.directory / (task + ".json"))

    def add_evidence_nodes(self):
        for task in self.graph.tasks:
            receipt = self.receipt(task)
            if receipt and self.prerequisites_pass(task):
                for result in receipt["results"]:
                    key = task + "." + result["id"]
                    self.graph.nodes["evidence:" + key] = {
                        "id": key, "type": "evidence", "task": task, "snapshot": self.state, **{
                            field: result[field] for field in ("tests", "exit_code")},
                    }
                    self.graph.edge("check", result["id"], "observed_as", "evidence", key)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest="command", required=True)
    for name in ("ready", "validate", "graph"):
        subs.add_parser(name)
    for name in ("show", "impact", "run"):
        subs.add_parser(name).add_argument("id")
    subs.add_parser("loop").add_argument("--limit", type=int, choices=range(1, MAX_STEPS + 1), default=1)
    args = parser.parse_args(argv)
    try:
        session = Session(ROOT)
        graph = session.graph
        failed = False
        if args.command == "validate":
            from check_catalog_links import verify
            catalog = verify(commands_json=None, write_overview=False)
            out = dict(valid=True, catalog=catalog, features=len(graph.features), tasks=len(graph.tasks),
                       criteria=len(graph.criteria), checks=len(graph.checks))
        elif args.command in ("graph", "show", "impact"):
            session.add_evidence_nodes()
            out = (dict(nodes=graph.nodes, edges=graph.edges) if args.command == "graph"
                   else graph.query(args.id, args.command == "impact"))
        elif args.command == "ready":
            states = {key: session.status(key) for key in graph.tasks}
            counts = {state: list(states.values()).count(state) for state in sorted(set(states.values()))}
            out = {"snapshot": session.state, "counts": counts, "tasks": states}
        elif args.command == "run":
            out = session.execute(args.id)
            failed = not all(check["passed"] for check in out["results"])
        else:
            demand(session.state["clean"], "verification needs a clean commit")
            runs = []
            for _ in range(args.limit):
                task = next((key for key in graph.tasks if session.status(key) == "ready"), None)
                if task is None:
                    break
                row = session.execute(task)
                runs.append(row)
                if not all(check["passed"] for check in row["results"]):
                    failed = True
                    break
            out = dict(runs=runs, limit=args.limit, stop="failed" if failed else
                       ("limit" if len(runs) == args.limit else "no_ready_checks"))
        print(json.dumps(out, ensure_ascii=False))
        return int(failed)
    except (OSError, KeyError, ValueError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 2


if __name__ == "__main__":
    sys.exit(main())
