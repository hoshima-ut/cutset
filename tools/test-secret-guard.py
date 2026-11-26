#!/usr/bin/env python3
"""Exercise Cutset hooks against disposable repositories, without network access."""

import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
TOKEN = "gh" + "p_" + hashlib.sha256(b"cutset synthetic marker").hexdigest()[:36]
ZERO = "0" * 40


class SecretGuardTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        home = Path(temp.name)
        self.repo = home / "working"
        self.repo.mkdir()
        self.remote = home / "remote.git"
        self.env = {**os.environ, "HOME": str(home), "XDG_CONFIG_HOME": str(home),
                    "GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                    "GIT_AUTHOR_NAME": "Tester", "GIT_AUTHOR_EMAIL": "test@example.invalid",
                    "GIT_COMMITTER_NAME":"Tester", "GIT_COMMITTER_EMAIL":"test@example.invalid"}
        for key in ("GIT_DIR","GIT_INDEX_FILE","GIT_COMMON_DIR","GIT_WORK_TREE"):
            self.env.pop(key, None)
        self.git("init", "-q", "-b", "main")
        self.git("init", "-q", "--bare", str(self.remote))
        self.git("commit", "-q", "--allow-empty", "-m", "Initial")
        self.first = self.git("rev-parse", "HEAD").strip()

    def execute(self, args, data=None):
        return subprocess.run(args, cwd=self.repo, env=self.env, input=data, text=True,
                              capture_output=True)

    def git(self, *args):
        proc = self.execute(["git", *args])
        self.assertEqual(proc.returncode,0,"Git fixture setup failed")
        return proc.stdout

    def write(self, path, data):
        p = self.repo/path
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_bytes(data if isinstance(data,bytes) else data.encode())

    def guard(self, *args, data=None, ok):
        proc = self.execute([str(ROOT/"tools/secret-guard"), *args], data)
        self.assertNotIn(TOKEN, proc.stdout+proc.stderr)
        self.assertEqual(proc.returncode == 0, ok, "Unexpected guard result: "+proc.stderr)

    def push_guard(self, ok, ref="HEAD", remote_old=ZERO):
        oid=self.git("rev-parse",ref).strip()
        line=f"{ref} {oid} refs/heads/test {remote_old}\n"
        self.guard("pre-push","origin",str(self.remote),data=line,ok=ok)

    def test_exact_index_and_binary(self):
        self.write("sample.txt","clean")
        self.git("add","sample.txt")
        self.write("sample.txt",TOKEN)
        self.guard("staged",ok=True)
        self.git("add","sample.txt")
        self.write("sample.txt","clean")
        self.guard("staged",ok=False)
        self.git("add","sample.txt")
        self.write("picture.bin",b"\x00header\x00"+TOKEN.encode()+b"\x00trailer")
        self.git("add","picture.bin")
        self.guard("staged",ok=False)

        for encoding in ("utf-16-le","utf-16-be"):
            self.write("picture.bin",b"\x80\xff"+TOKEN.encode(encoding))
            self.git("add","picture.bin")
            self.guard("staged",ok=False)

    def test_denied_names_and_bypass_settings(self):
        self.write("nested/.env.production","plain")
        shutil.copy2(ROOT/".gitignore",self.repo/".gitignore")
        self.assertEqual(self.execute(["git","add","nested/.env.production"]).returncode,1)
        self.git("add","-f","nested/.env.production")
        self.guard("staged",ok=False)
        self.git("reset","-q")
        for filename in (".git-credentials", ".pgpass"):
            self.write(filename, "dummy")
            self.assertEqual(self.execute(["git","add",filename]).returncode,1)
            self.git("add","-f",filename)
            self.guard("staged",ok=False)
            self.git("reset","-q")
        self.write("example.txt",TOKEN+" # gitleaks:allow")
        self.write(".gitleaks.toml",'title = "do not trust"\n')
        self.env["GITLEAKS_CONFIG"] = str(self.repo/".gitleaks.toml")
        self.git("add","example.txt")
        self.guard("staged",ok=False)

    def test_disguised_archive_is_opaque(self):
        self.write("opaque.asset",b"PK\x03\x04"+bytes(20))
        self.git("add","opaque.asset")
        self.guard("staged",ok=False)

    def test_lfs_pointer_cannot_certify_external_payload(self):
        self.write("clip.dat","version https://git-lfs.github.com/spec/v1\noid sha256:"+"a"*64+"\nsize 12\n")
        self.git("add","clip.dat")
        self.guard("staged",ok=False)

    def test_removed_secret_on_new_and_existing_branches(self):
        self.git("push","-q",str(self.remote),"main")
        self.write("sample.txt",TOKEN)
        self.git("add","sample.txt")
        self.git("commit","-qm","Add sample")
        self.git("rm","-q","sample.txt")
        self.git("commit","-qm","Delete sample")
        self.push_guard(False)
        self.push_guard(False,remote_old=self.first)
        self.git("update-ref","refs/remotes/origin/stale",self.git("rev-parse","HEAD").strip())
        self.push_guard(False)

    def test_new_safe_branch_and_tag_message(self):
        self.git("push","-q",str(self.remote),"main")
        self.git("commit","--allow-empty","-qm","Good change")
        self.push_guard(True)
        self.git("tag","-a","test-pilot","-m",TOKEN)
        self.push_guard(False,"refs/tags/test-pilot")

    def test_merge_result_and_commit_message(self):
        self.git("switch","-qc","second")
        self.write("second","second")
        self.git("add","second")
        self.git("commit","-qm","Second")
        self.git("switch","-q","main")
        self.write("first","first")
        self.git("add","first")
        self.git("commit","-qm","First")
        self.git("merge","--no-ff","--no-commit","second")
        self.write("merge-only",TOKEN)
        self.git("add","merge-only")
        self.git("commit","-qm","Merge")
        self.push_guard(False)
        self.git("switch","--detach",self.first)
        self.git("commit","--allow-empty","-qm",TOKEN)
        self.push_guard(False)

    def test_installer_preserves_active_hooks(self):
        for file in (".githooks/pre-commit",".githooks/pre-push","tools/secret-guard","tools/install-hooks"):
            path=self.repo/file
            path.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(ROOT/file,path)
        installer=[str(self.repo/"tools/install-hooks")]
        self.git("config","--local","core.hooksPath","other")
        self.assertNotEqual(self.execute(installer).returncode,0)
        self.assertEqual(self.git("config","--get","core.hooksPath").strip(),"other")
        self.git("config","--unset","core.hooksPath")
        hook=self.repo/".git/hooks/commit-msg"
        hook.write_text("#!/bin/sh\nexit 0\n")
        hook.chmod(0o755)
        self.assertNotEqual(self.execute(installer).returncode,0)
        self.assertTrue(hook.exists())
        hook.unlink()
        self.assertEqual(self.execute(installer).returncode,0)
        self.assertEqual(self.execute(installer).returncode,0)
        installed=Path(self.git("config","--get","core.hooksPath").strip())
        self.assertTrue(installed.is_absolute() and installed.is_dir())
        self.git("add",".githooks","tools")
        self.git("commit","-qm","Add hook source")
        self.git("switch","--detach",self.first)
        self.assertFalse((self.repo/"tools/secret-guard").exists())
        self.write("secret",TOKEN)
        self.git("add","secret")
        attempted=self.execute(["git","commit","-qm","Should block"])
        self.assertNotEqual(attempted.returncode,0)
        self.assertNotIn(TOKEN,attempted.stdout+attempted.stderr)
        # Simulate a commit received from a contributor whose local hooks were absent.
        self.git("-c", "core.hooksPath=/dev/null", "commit", "-qm", "Imported change")
        sent = self.execute(["git","push",str(self.remote),"HEAD:refs/heads/share"])
        self.assertNotEqual(sent.returncode,0)
        self.assertNotIn(TOKEN,sent.stdout+sent.stderr)
        self.assertEqual(self.git("ls-remote","--heads",str(self.remote)),"")


if __name__ == "__main__":
    unittest.main()
