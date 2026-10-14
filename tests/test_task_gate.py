"""Exercise the Stop hook against real temporary Git repositories."""

import json
from pathlib import Path
import subprocess
import tempfile
import unittest


HOOK = Path(__file__).resolve().parents[1] / "hooks/task-gate.sh"


class TaskGateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='taskops "repo" ')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.git("init", "-q")

    def git(self, *args):
        subprocess.run(
            ["git", *args], cwd=self.root, check=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )

    def write(self, name, text="example\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        return path

    def task(self, name="task", docker=False):
        for path in ("task.toml", "instruction.md", "tests/test.sh", "README.md"):
            self.write(f"{name}/{path}")
        if docker:
            self.write(f"{name}/environment/Dockerfile")

    def commit(self):
        self.git("add", "--all")
        self.git("-c", "user.name=TaskOps Test", "-c", "user.email=test@example.com",
                 "commit", "-qm", "fixture")

    def run_hook(self, payload=None, raw=None):
        if raw is None:
            raw = json.dumps(payload if payload is not None else {"cwd": str(self.root)})
        result = subprocess.run(
            ["sh", str(HOOK)], input=raw, text=True, cwd=self.root,
            capture_output=True, timeout=12,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stderr, "")
        return result.stdout

    def test_untracked_task_with_spaces_and_optional_docker(self):
        self.task('nested/task with "quotes" [1]')
        out = self.run_hook()
        self.assertIn('nested/task with "quotes" [1]: task files changed (SUBSTANTIVE)', out)
        self.assertIn("structure ok", out)
        self.assertNotIn("MISSING", out)
        self.assertIn("before commit", out)

    def test_nested_cwd_uses_repository_relative_paths(self):
        self.task("nested/task")
        out = self.run_hook({"cwd": str(self.root / "nested/task/tests")})
        self.assertIn("nested/task: task files changed", out)

    def test_clean_tree_and_unrelated_readme_are_silent(self):
        self.task()
        self.commit()
        self.assertEqual(self.run_hook(), "")
        self.write("README.md")
        self.assertEqual(self.run_hook(), "")

    def test_json_guard_and_invalid_inputs_are_nonblocking(self):
        self.task()
        self.assertEqual(self.run_hook({"cwd": str(self.root), "stop_hook_active": True}), "")
        for raw in ("not json", "[]", "null", '{"cwd": null}', '{"cwd": 3}'):
            self.assertEqual(self.run_hook(raw=raw), "")

    def test_rename_reports_missing_source_spec(self):
        self.task(docker=True)
        self.commit()
        self.git("mv", "task/instruction.md", "task/old spec.md")
        out = self.run_hook()
        self.assertIn("MISSING: instruction.md", out)
        self.assertIn("SUBSTANTIVE", out)

    def test_deleted_verifier_is_reported(self):
        self.task(docker=True)
        self.commit()
        self.git("rm", "task/tests/test.sh")
        self.assertIn("MISSING: tests/test.sh", self.run_hook())

    def test_documentation_does_not_disable_review(self):
        self.task()
        self.commit()
        self.write("task/README.md", "updated\n")
        out = self.run_hook()
        self.assertIn("DOCUMENTATION", out)
        self.assertIn("official review", out)
        self.assertNotIn("no review needed", out)

    def test_scratch_files_do_not_trigger_hook(self):
        self.task()
        self.commit()
        for path in (".review/tests/report.md", "jobs/tests/log.txt", "results/instruction.md"):
            self.write(f"task/{path}")
        self.assertEqual(self.run_hook(), "")

    def test_summary_preserves_guidance_for_many_tasks(self):
        for i in range(8):
            self.task(f"task-{i}")
        out = self.run_hook()
        self.assertIn("2 additional affected task directories", out)
        self.assertIn("before commit", out.splitlines()[-1])
        self.assertLessEqual(len(out.splitlines()), 8)

    def test_unknown_layout_does_not_claim_tbench_validity(self):
        self.write("site/site.toml")
        self.write("site/instruction.md")
        out = self.run_hook()
        self.assertIn("layout checks deferred to track profile", out)
        self.assertNotIn("structure ok", out)


if __name__ == "__main__":
    unittest.main()
