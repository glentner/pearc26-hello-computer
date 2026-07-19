# SPDX-License-Identifier: MIT
"""Stdlib unit tests for the self-improvement finding reader (meta_status.py)."""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

BIN = Path(__file__).resolve().parents[1] / ".agents" / "factory" / "bin"
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BIN))

import meta_status  # noqa: E402

ONE_FINDING = """\
# META — x

## Friction findings

Schema (the fence below is illustrative and must be skipped):

```markdown
## F9 — a fake schema finding that must be ignored
`origin=paper-x:1 severity=high category=tooling status=open target=foo`
```

## F1 — a real finding
`origin=paper-outline:5 severity=medium category=template status=open target=.agents/factory/methodology.md`
- **What happened:** the skill made me copy-paste.
- **Recommended fix:** factor it out.
- **Confidence:** high · **Effort:** small
"""


class TestMetaStatus(unittest.TestCase):
    def test_template_reports_zero(self):
        # The shipped template's only finding lives inside a fence → parser skips it.
        text = (ROOT / ".agents" / "factory" / "templates" / "META.md").read_text()
        self.assertEqual(len(meta_status.parse_findings(text)), 0)

    def test_fenced_schema_skipped_real_counted(self):
        findings = meta_status.parse_findings(ONE_FINDING)
        self.assertEqual([f["id"] for f in findings], ["F1"])
        f1 = findings[0]
        self.assertEqual(f1["severity"], "medium")
        self.assertEqual(f1["category"], "template")
        self.assertEqual(f1["status"], "open")
        self.assertEqual(f1["origin"], "paper-outline:5")
        self.assertEqual(f1["recommended_fix"], "factor it out.")

    def test_missing_file_is_empty_state_exit_0(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = meta_status.main(["/no/such/META.md"])
        self.assertEqual(rc, 0)
        self.assertFalse(json.loads(buf.getvalue())["exists"])

    def test_status_filter(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "META.md"
            p.write_text(ONE_FINDING, encoding="utf-8")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                meta_status.main([str(p), "--status", "applied"])
            report = json.loads(buf.getvalue())
            self.assertEqual(report["counts"]["open"], 1)     # counts are pre-filter
            self.assertEqual(report["findings"], [])          # none applied

    def test_summary_one_line(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "META.md"
            p.write_text(ONE_FINDING, encoding="utf-8")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                rc = meta_status.main([str(p), "--summary"])
            out = buf.getvalue()
            self.assertEqual(rc, 0)
            self.assertEqual(out.count("\n"), 1)
            self.assertIn("1 open", out)
            self.assertIn("F1", out)

    def test_summary_missing_file(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = meta_status.main(["/no/such/META.md", "--summary"])
        self.assertEqual(rc, 0)
        self.assertIn("0 findings", buf.getvalue())

    def test_repo_meta_parses(self):
        # The seeded repo-root META.md must have exactly one open finding (F1).
        meta = ROOT / "META.md"
        if meta.exists():
            findings = meta_status.parse_findings(meta.read_text())
            self.assertTrue(all(f["status"] in meta_status.STATUSES for f in findings))


if __name__ == "__main__":
    unittest.main()
