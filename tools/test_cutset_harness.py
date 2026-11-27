"""Offline regression tests for the Cutset verification loop."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unicodedata import normalize
from unittest.mock import patch

from cutset_harness import Graph, cargo_tests, command, minimum
from feature_docs import PAGES, check_pages, indexes

ROOT = Path(__file__).resolve().parents[1]
FEATURE = {"id": "AI-03", "title": "プレビュー 候補", "category": "ai-plugin",
           "scope": "Read the plan.", "acceptance": "Read the preview."}
PASS = """import unittest
class Contract(unittest.TestCase):
    def test_acceptance(self):
        self.assertTrue(True)
if __name__ == "__main__":
    unittest.main()
"""


def manifest():
    """The Python part of the real graph: fixture repositories have no Rust workspace."""
    cfg = json.loads((ROOT / "docs/specs/data/graph.json").read_text(encoding="utf-8"))
    rust = {check["id"] for check in cfg["checks"] if "cargo" in check}
    criteria = {row["id"] for row in cfg["acceptance"] if set(row["checks"]) & rust}
    return dict(checks=[c for c in cfg["checks"] if c["id"] not in rust],
                acceptance=[a for a in cfg["acceptance"] if a["id"] not in criteria],
                tasks=[t for t in cfg["tasks"] if not set(t["acceptance"]) & criteria])


class GraphTest(unittest.TestCase):
    def test_duplicate_unknown_cycle_rejected(self):
        for fault, msg in (("duplicate", "duplicate"), ("unknown", "unknown"),
                           ("cycle", "cycle"), ("command", "unsupported"),
                           ("string", "invalid"), ("orphan", "orphan")):
            with self.subTest(fault=fault):
                cfg = manifest()
                task = cfg["tasks"][0]
                if fault == "duplicate":
                    cfg["tasks"].append(task)
                if fault == "unknown":
                    task["requires"] = ["MISSING"]
                if fault == "cycle":
                    task["requires"] = ["CHECK-PREVIEW"]
                if fault == "command":
                    cfg["checks"][0]["argv"] = ["python3", "-c", "pass"]
                if fault == "string":
                    task["requires"] = "CHECK-PREVIEW"
                if fault == "orphan":
                    cfg["acceptance"].append(dict(id="UNUSED", description="test", checks=[]))
                with self.assertRaisesRegex(ValueError, msg):
                    Graph({"features": [FEATURE]}, cfg)

    def test_trace_to_component_and_backlog(self):
        graph = Graph({"features": [FEATURE]}, manifest())
        impact = graph.query("AI-03", transitive=True)["reachable"]
        self.assertIn("check:PREVIEW-TESTS", impact)
        self.assertIn("acceptance:AC-AI-03", impact)
        self.assertNotIn("check:HARNESS-TESTS", impact)
        self.assertEqual(graph.checks_for("BUILD-AI-03"), [])
        self.assertEqual(graph.query("task:CHECK-PREVIEW")["node"]["type"], "task")

    def test_feature_promotion_keeps_catalog_acceptance(self):
        cfg = manifest()
        cfg["acceptance"].append({"id": "AC-AI-03", "checks": ["PREVIEW-TESTS"]})
        graph = Graph({"features": [FEATURE]}, cfg)
        self.assertEqual(graph.checks_for("BUILD-AI-03"), ["PREVIEW-TESTS"])
        self.assertEqual(graph.criteria["AC-AI-03"]["description"], FEATURE["acceptance"])
        cfg["acceptance"][-1]["description"] = "a weaker condition"
        with self.assertRaisesRegex(ValueError, "catalog acceptance"):
            Graph({"features": [FEATURE]}, cfg)


CARGO = {"package": "filmcraft-interchange", "test": "it", "filter": "fcp7::", "min_tests": 19}


class CargoCheckTest(unittest.TestCase):
    def graph_with(self, cargo):
        cfg = manifest()
        cfg["checks"].append({"id": "RUST-TESTS", "cargo": cargo})
        cfg["acceptance"].append({"id": "AC-AI-03", "checks": ["RUST-TESTS"]})
        return Graph({"features": [FEATURE]}, cfg, packages={"filmcraft-interchange"})

    def test_cargo_check_builds_a_fixed_command(self):
        graph = self.graph_with(CARGO)
        self.assertEqual(command(graph.checks["RUST-TESTS"]),
                         ["cargo", "test", "--locked", "-p", "filmcraft-interchange", "--test", "it", "--", "fcp7::"])
        self.assertEqual(graph.checks_for("BUILD-AI-03"), ["RUST-TESTS"])
        self.assertEqual(minimum(graph.checks["RUST-TESTS"]), 19)

    def test_cargo_check_rejects_unknown_package_and_shell_text(self):
        for fault in ({"package": "other-crate"}, {"filter": "fcp7; rm -rf /"}, {"test": "../it"},
                      {"extra": "--release"}, {"package": 3}, {"min_tests": 0}, {"min_tests": "19"}):
            with self.subTest(fault=fault):
                with self.assertRaisesRegex(ValueError, "cargo"):
                    self.graph_with(dict(CARGO, **fault))

    def test_cargo_summary_counts_every_binary_and_rejects_failures(self):
        ok = "test result: ok. 3 passed; 0 failed; 0 ignored\n\ntest result: ok. 2 passed; 0 failed\n"
        self.assertEqual(cargo_tests(ok), 5)
        self.assertEqual(cargo_tests("test result: ok. 0 passed; 0 failed\n"), 0)
        self.assertEqual(cargo_tests(ok + "test result: FAILED. 1 passed; 1 failed\n"), 0)
        self.assertEqual(cargo_tests("error[E0432]: unresolved import\n"), 0)


class LoopTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.base = Path(tmp.name)
        (self.base / "tools").mkdir()
        (self.base / "docs/specs/data").mkdir(parents=True)
        self.write(".gitignore", "/target/\n__pycache__/\n")
        for name in ("cutset_harness.py", "feature_docs.py"):
            shutil.copy(ROOT / "tools" / name, self.base / "tools")
        directory = self.base / "docs/specs/ai-plugin" / FEATURE["title"]
        directory.mkdir(parents=True)
        bodies = {"目的と範囲": FEATURE["scope"], "受入条件": FEATURE["acceptance"]}
        for name, headings in PAGES.items():
            label = {"requirements.md": "要件", "design.md": "設計", "tasks.md": "作業・試験"}[name]
            text = f"# {FEATURE['title']}の{label}（AI-03）\n"
            for heading in headings:
                text += f"\n## {heading}\n\n{bodies.get(heading, 'Fixture detail.')}\n"
            (directory / name).write_text(text, encoding="utf-8")
        self.write("tools/test_cutset_harness.py", PASS)
        self.write("tools/test_cutset_trial.py", PASS)
        self.write("docs/specs/data/catalog.json", json.dumps({"features": [FEATURE]}))
        self.write("docs/specs/data/graph.json", json.dumps(manifest()))
        self.git("init", "-q")
        self.commit("fixture")

    def git(self, *args):
        return subprocess.check_output(["git", "-c", "user.name=Fixture", "-c",
                                        "user.email=fixture@example.invalid", "-c", "commit.gpgsign=false",
                                        "-c", "core.hooksPath=/dev/null", *args], cwd=self.base, text=True)

    def write(self, name, value):
        (self.base / name).write_text(value, encoding="utf-8")

    def commit(self, message):
        self.git("add", ".")
        self.git("commit", "-qm", message)

    def cli(self, *args, code=0):
        proc = subprocess.run([sys.executable, "tools/cutset_harness.py", *args], cwd=self.base,
                              capture_output=True, text=True)
        self.assertEqual(proc.returncode, code, proc.stdout + proc.stderr)
        return json.loads(proc.stdout)

    def test_bounded_loop_and_invalidation(self):
        self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "blocked")
        self.assertIn("planned", self.cli("run", "BUILD-AI-03", code=2)["error"])
        runs = self.cli("loop", "--limit", "1")["runs"]
        self.assertEqual([row["task"] for row in runs], ["HARNESS-CONTRACT"])
        self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "ready")
        runs = self.cli("loop", "--limit", "5")["runs"]
        self.assertEqual([row["task"] for row in runs], ["CHECK-PREVIEW"])
        self.assertEqual(self.cli("loop")["stop"], "no_ready_checks")
        self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "review_pending")
        evidence = "evidence:CHECK-PREVIEW.PREVIEW-TESTS"
        self.assertIn(evidence, self.cli("impact", "AI-03")["reachable"])
        self.write("notes.md", "changed inputs")
        self.assertFalse(self.cli("ready")["snapshot"]["clean"])
        self.assertNotIn(evidence, self.cli("graph")["nodes"])
        self.cli("loop", code=2)
        self.commit("update")
        self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "blocked")

    def test_decomposed_listing_and_normalization_collision(self):
        spec = self.base / "docs/specs"
        category = spec / FEATURE["category"]
        for forms in (["NFD"], ["NFC", "NFD"]):
            with self.subTest(forms=forms):
                def listed(pattern):
                    name = Path(pattern).name
                    return [category / normalize(form, FEATURE["title"]) / name for form in forms]

                with patch.object(Path, "glob", side_effect=listed):
                    if len(forms) == 1:
                        self.assertIn("AI-03", check_pages(spec, [FEATURE]))
                    else:
                        with self.assertRaisesRegex(ValueError, "duplicate normalized"):
                            check_pages(spec, [FEATURE])

    def test_spec_links_resolve_after_title_change(self):
        spec = self.base / "docs/specs"
        row = dict(FEATURE, title="音声のプレビュー #2（新）", baselineDisposition="verify", milestone="M1")
        directory = spec / row["category"] / row["title"]
        (directory.parent / FEATURE["title"]).rename(directory)
        for name in PAGES:
            p = directory / name
            p.write_text(p.read_text(encoding="utf-8").replace(FEATURE["title"], row["title"]), encoding="utf-8")
        self.write("docs/specs/data/catalog.json", json.dumps({"features": [row]}))
        self.commit("rename feature while keeping graph ID")
        self.assertEqual(self.cli("show", "AC-AI-03")["node"]["description"], row["acceptance"])
        index = indexes(spec, [row])[directory.parent / "README.md"]
        self.assertIn("(音声のプレビュー%20%232（新）/design.md)", index)
        p = directory / "design.md"
        p.write_text(p.read_text(encoding="utf-8").replace("（AI-03）", "（AI-04）"), encoding="utf-8")
        self.assertIn("AI-03", self.cli("show", "AI-03", code=2)["error"])

    def test_clean_commit_with_stale_requirements_is_rejected(self):
        page = self.base / "docs/specs/ai-plugin" / FEATURE["title"] / "requirements.md"
        page.write_text(page.read_text(encoding="utf-8").replace(
            FEATURE["acceptance"], "Read the revised preview."), encoding="utf-8")
        self.commit("change canonical acceptance")
        for args in (("show", "AI-03"), ("ready",), ("run", "HARNESS-CONTRACT"), ("loop",)):
            with self.subTest(args=args):
                self.assertIn("AI-03", self.cli(*args, code=2)["error"])
        self.assertFalse((self.base / "target").exists())
        updated = dict(FEATURE, acceptance="Read the revised preview.")
        self.write("docs/specs/data/catalog.json", json.dumps({"features": [updated]}))
        self.commit("refresh projection")
        self.assertEqual(self.cli("show", "AC-AI-03")["node"]["description"], updated["acceptance"])
        self.assertTrue(self.cli("run", "HARNESS-CONTRACT")["results"][0]["passed"])

    def test_malformed_receipt_is_ignored(self):
        row = self.cli("run", "HARNESS-CONTRACT")
        path = self.base / "target" / "cutset-harness" / row["snapshot"]["revision"] / "HARNESS-CONTRACT.json"
        row["results"][0]["argv"] = ["python3", "different.py"]
        path.write_text(json.dumps(row))
        self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "blocked")
        path.write_text("invalid JSON")
        self.assertEqual(self.cli("ready")["tasks"]["HARNESS-CONTRACT"], "ready")

    def test_double_run_and_changing_inputs_do_not_grant_evidence(self):
        revision = self.git("rev-parse", "HEAD").strip()
        lock = self.base / "target" / "cutset-harness" / revision / ".running"
        lock.mkdir(parents=True)
        self.assertIn("lock", self.cli("run", "HARNESS-CONTRACT", code=2)["error"])
        self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "blocked")
        self.write("tools/test_cutset_harness.py",
                   'from pathlib import Path\nPath("docs/specs/data/graph.json").touch()\n'
                   'Path("changed.txt").write_text("changed during check")\n' + PASS)
        self.commit("check modifies its worktree")
        self.assertIn("changed", self.cli("run", "HARNESS-CONTRACT", code=2)["error"])
        self.assertFalse(self.cli("ready")["snapshot"]["clean"])

    def test_zero_tests_and_failure_stop_loop(self):
        for script in ("pass\n", "import sys\nsys.exit(1)\n"):
            with self.subTest(script=script):
                self.write("tools/test_cutset_harness.py", script)
                self.commit("change check")
                out = self.cli("loop", "--limit", "3", code=1)
                self.assertEqual(out["stop"], "failed")
                self.assertEqual(len(out["runs"]), 1)
                self.assertEqual(self.cli("ready")["tasks"]["CHECK-PREVIEW"], "blocked")


if __name__ == "__main__":
    unittest.main()
