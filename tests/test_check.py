"""Exercise the checker on isolated copies; never mutate the real repository."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CheckerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(".git", "__pycache__", ".venv"))

    def run_check(self, *args):
        return subprocess.run(
            [sys.executable, str(self.repo / "scripts/check.py"), *args],
            capture_output=True, text=True, check=False,
        )

    def test_clean_repository_and_repeated_sync(self):
        entry = self.repo / "UNWALL.md"
        before = entry.read_bytes(), entry.stat().st_mtime_ns
        self.assertEqual(self.run_check().returncode, 0)
        self.assertEqual(self.run_check("--sync").returncode, 0)
        self.assertEqual(self.run_check("--sync").returncode, 0)
        self.assertEqual((entry.read_bytes(), entry.stat().st_mtime_ns), before)

    def test_stale_entry_is_detected_without_rewriting(self):
        entry = self.repo / "UNWALL.md"
        entry.write_text("stale\n", encoding="utf-8")
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("differs", result.stderr)
        self.assertEqual(entry.read_text(encoding="utf-8"), "stale\n")
        self.assertEqual(self.run_check("--sync").returncode, 0)

    def test_missing_local_reference_fails(self):
        (self.repo / "docs/probe.md").write_text("[Missing](absent.md)\n", encoding="utf-8")
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("missing local link", result.stderr)

    def test_parent_escape_fails_even_when_target_exists(self):
        (self.repo.parent / "outside.md").write_text("outside", encoding="utf-8")
        (self.repo / "probe.md").write_text("[Outside](../outside.md)\n", encoding="utf-8")
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("leaves repository", result.stderr)

    def test_external_urls_fragments_and_code_are_not_files(self):
        (self.repo / "probe.md").write_text(
            "[External](https://example.invalid/missing)\n"
            "[Section](#missing)\n```md\n[Example](missing.md)\n```\n",
            encoding="utf-8",
        )
        self.assertEqual(self.run_check().returncode, 0)

    def test_bad_skill_metadata_fails(self):
        skill = self.repo / "skills/unwalled-garden/SKILL.md"
        skill.write_text(skill.read_text(encoding="utf-8").replace("name: unwalled-garden", "name: wrong-name"), encoding="utf-8")
        result = self.run_check()
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("skill name", result.stderr)


if __name__ == "__main__":
    unittest.main()
