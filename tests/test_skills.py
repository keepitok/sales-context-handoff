"""Check that the indexed workflow and starter remain portable when copied."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/sales-context-handoff"
STAGES = ("01-setup.md", "02-collect.md", "03-analyze.md", "04-handoff.md")


class SkillTests(unittest.TestCase):
    def test_copied_skill_index_resolves_stages_resources_and_licenses(self):
        with tempfile.TemporaryDirectory() as temporary:
            skill = Path(temporary) / "sales-context-handoff"
            shutil.copytree(SKILL, skill, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            self.assertTrue((skill / "agents/openai.yaml").is_file())
            self.assertEqual((ROOT / "LICENSE").read_bytes(), (skill / "LICENSE").read_bytes())
            self.assertIn("name: sales-context-handoff\n", (skill / "SKILL.md").read_text(encoding="utf-8"))

            # Follow the installed index's actual links, including secondary references.
            visited = set()
            pending = [skill / "SKILL.md"]
            while pending:
                document = pending.pop().resolve()
                if document in visited:
                    continue
                visited.add(document)
                if document.suffix != ".md":
                    continue
                body = document.read_text(encoding="utf-8")
                for target in re.findall(r"\]\(([^\s)]+)\)", body):
                    if urlsplit(target).scheme:
                        continue
                    # These are examples of citations in future user reports.
                    if re.fullmatch(r"\.\./extracts/ev-\d+\.md", target):
                        continue
                    resolved = (document.parent / target).resolve()
                    self.assertTrue(resolved.is_relative_to(skill.resolve()), target)
                    self.assertTrue(resolved.is_file(), f"{document.name}: {target}")
                    pending.append(resolved)

            for stage in STAGES:
                self.assertIn((skill / "references" / stage).resolve(), visited)
            for license_name in ("zarif-MIT.txt", "anthropic-Apache-2.0.txt", "checkpoint-MIT.txt"):
                installed = skill / "licenses" / license_name
                self.assertIn(installed.resolve(), visited)
                self.assertEqual((SKILL / "licenses" / license_name).read_bytes(), installed.read_bytes())

    def test_upstream_adaptation_targets_exist(self):
        mapping = json.loads((ROOT / "adaptation-map.json").read_text(encoding="utf-8"))
        for target in mapping["mapping"].values():
            resolved = (ROOT / mapping["mapping_root"] / target).resolve()
            self.assertTrue(resolved.is_relative_to(SKILL.resolve()), target)
            self.assertTrue(resolved.is_file(), target)

    def test_copied_starter_helper_runs_in_new_process(self):
        with tempfile.TemporaryDirectory() as temporary:
            workspace = Path(temporary) / "sales-context-workspace"
            shutil.copytree(SKILL / "assets/workspace", workspace,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            (workspace / "gitignore.template").rename(workspace / ".gitignore")
            self.assertEqual((ROOT / "LICENSE").read_bytes(), (workspace / "LICENSE").read_bytes())
            for folder in ("raw", "working", "handoff"):
                self.assertTrue((workspace / folder).is_dir())
            result = subprocess.run([sys.executable, "tools/context_tools.py", "validate", "."],
                                    cwd=workspace, text=True, capture_output=True)
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            self.assertEqual(0, json.loads(result.stdout)["counts"]["deals"])


if __name__ == "__main__":
    unittest.main()
