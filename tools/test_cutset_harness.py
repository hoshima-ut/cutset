"""Offline regression tests for the Cutset verification loop."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from cutset_harness import Graph
from feature_docs import PAGES

ROOT = Path(__file__).resolve().parents[1]
FEATURE = {"id": "AI-03", "title": "Proposal preview", "category": "ai-plugin",
           "scope": "Read the plan.", "acceptance": "Read the preview."}
PASS = """import unittest
class Contract(unittest.TestCase):
    def test_acceptance(self):
        self.assertTrue(True)
if __name__ == "__main__":
    unittest.main()
"""


def manifest():
    return json.loads((ROOT / "docs/specs/data/graph.json").read_text(encoding="utf-8"))


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
        directory = self.base / "docs/specs/ai-plugin/AI-03"
        directory.mkdir(parents=True)
        bodies = {"目的と範囲": FEATURE["scope"], "受入条件": FEATURE["acceptance"]}
        for name, headings in PAGES.items():
            text = "# AI-03 Proposal preview\n"
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

    def test_clean_commit_with_stale_requirements_is_rejected(self):
        page = self.base / "docs/specs/ai-plugin/AI-03/requirements.md"
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
