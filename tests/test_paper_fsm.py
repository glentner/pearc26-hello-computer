# SPDX-License-Identifier: MIT
"""Stdlib unit tests for the paper-factory FSM scripts (_fsm / set_status / paper_status).

No third-party deps — run with `python3 -m unittest discover -s tests` or `make test`.
"""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

BIN = Path(__file__).resolve().parents[1] / ".agents" / "factory" / "bin"
sys.path.insert(0, str(BIN))

import _fsm  # noqa: E402
import set_status  # noqa: E402
import paper_status  # noqa: E402

VALID = """\
---
slug: t
title: "T: a paper"
venue: PEARC26
macro_phase: outlining
base: main
branch: draft
last_updated: 2026-07-18
sections:
  - {id: 01-intro, status: draft, satisfies: [C1], target_words: 100, order: 1}
  - {id: 02-body, status: review, satisfies: [], target_words: 200, order: 2}
claims:
  - {id: C1, status: proposed, satisfied_by: [01-intro], evidence: []}
review: {cycle: 0, verdict: none}
---

# body preserved verbatim
"""


class TestFsm(unittest.TestCase):
    def test_builtin_selftest_passes(self):
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(_fsm._selftest(), 0)

    def test_roundtrip_byte_stable(self):
        data, body = _fsm.split_frontmatter(VALID)
        self.assertEqual(_fsm.dump_document(data, body), VALID)

    def test_crlf_parses_without_stray_cr(self):
        data, _ = _fsm.split_frontmatter(VALID.replace("\n", "\r\n"))
        self.assertEqual(data["title"], "T: a paper")
        self.assertEqual(_fsm.validate(data), [])

    def test_validate_rejects_bad_macro_phase(self):
        data, _ = _fsm.split_frontmatter(VALID)
        data["macro_phase"] = "bogus"
        self.assertTrue(_fsm.validate(data))

    def test_validate_rejects_duplicate_section_id(self):
        data, _ = _fsm.split_frontmatter(VALID)
        data["sections"].append({"id": "01-intro", "status": "draft"})
        self.assertTrue(any("duplicate section id" in e for e in _fsm.validate(data)))

    def test_validate_rejects_negative_attempts(self):
        data, _ = _fsm.split_frontmatter(VALID)
        data["sections"][0]["attempts"] = -1
        self.assertTrue(any("attempts" in e for e in _fsm.validate(data)))

    def test_validate_rejects_bad_satisfies_ref(self):
        data, _ = _fsm.split_frontmatter(VALID)
        data["sections"][0]["satisfies"] = ["C9"]
        self.assertTrue(any("unknown claim" in e for e in _fsm.validate(data)))

    def test_attempts_and_reviewed_commit_roundtrip(self):
        data, body = _fsm.split_frontmatter(VALID)
        data["sections"][0]["attempts"] = 2
        data["review"]["reviewed_commit"] = "abc1234"
        out = _fsm.dump_document(data, body)
        data2, _ = _fsm.split_frontmatter(out)
        self.assertEqual(data2["sections"][0]["attempts"], 2)
        self.assertEqual(data2["review"]["reviewed_commit"], "abc1234")
        self.assertEqual(_fsm.validate(data2), [])


def _write(tmp: Path, text: str = VALID) -> Path:
    p = tmp / "PAPER.md"
    p.write_text(text, encoding="utf-8")
    return p


class TestSetStatus(unittest.TestCase):
    def test_section_status_transition(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            self.assertEqual(set_status.main([str(p), "--section", "01-intro", "--status", "review"]), 0)
            data, _ = _fsm.split_frontmatter(p.read_text())
            self.assertEqual(data["sections"][0]["status"], "review")

    def test_unknown_section_returns_3(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(set_status.main([str(p), "--section", "99-x", "--status", "review"]), 3)

    def test_record_attempt_increments(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            set_status.main([str(p), "--section", "01-intro", "--record-attempt"])
            set_status.main([str(p), "--section", "01-intro", "--record-attempt"])
            data, _ = _fsm.split_frontmatter(p.read_text())
            self.assertEqual(data["sections"][0]["attempts"], 2)

    def test_reviewed_commit_set(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            set_status.main([str(p), "--reviewed-commit", "deadbee"])
            data, _ = _fsm.split_frontmatter(p.read_text())
            self.assertEqual(data["review"]["reviewed_commit"], "deadbee")

    def test_add_section_then_duplicate_refused(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            self.assertEqual(set_status.main(
                [str(p), "--add-section", "03-x", "--target-words", "50", "--order", "3"]), 0)
            data, _ = _fsm.split_frontmatter(p.read_text())
            self.assertIn("03-x", [s["id"] for s in data["sections"]])
            before = p.read_text()
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(set_status.main([str(p), "--add-section", "03-x"]), 2)  # duplicate
            self.assertEqual(p.read_text(), before)  # refused before write

    def test_add_claim(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            self.assertEqual(set_status.main([str(p), "--add-claim", "C2", "--satisfied-by", "02-body"]), 0)
            data, _ = _fsm.split_frontmatter(p.read_text())
            self.assertIn("C2", [c["id"] for c in data["claims"]])

    def test_add_evidence_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            set_status.main([str(p), "--claim", "C1", "--add-evidence", "vaswani2017attention"])
            set_status.main([str(p), "--claim", "C1", "--add-evidence", "vaswani2017attention"])
            data, _ = _fsm.split_frontmatter(p.read_text())
            self.assertEqual(data["claims"][0]["evidence"], ["vaswani2017attention"])

    def test_record_attempt_without_section_errors(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(set_status.main([str(p), "--record-attempt"]), 2)


class TestPaperStatus(unittest.TestCase):
    def _run(self, argv):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = paper_status.main(argv)
        return rc, buf.getvalue()

    def test_valid_reports_json(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            rc, out = self._run([str(p)])
            self.assertEqual(rc, 0)
            report = json.loads(out)
            for key in ("macro_phase", "sections_by_status", "completion", "warnings", "section_attempts"):
                self.assertIn(key, report)
            self.assertEqual(report["sections_by_status"]["review"], ["02-body"])

    def test_invalid_returns_2(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d), VALID.replace("macro_phase: outlining", "macro_phase: bogus"))
            with contextlib.redirect_stderr(io.StringIO()):
                rc, _ = self._run([str(p)])
            self.assertEqual(rc, 2)

    def test_attempts_warning_at_3(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            set_status.main([str(p), "--section", "01-intro", "--record-attempt"])
            set_status.main([str(p), "--section", "01-intro", "--record-attempt"])
            set_status.main([str(p), "--section", "01-intro", "--record-attempt"])
            _, out = self._run([str(p)])
            report = json.loads(out)
            self.assertEqual(report["section_attempts"].get("01-intro"), 3)
            self.assertTrue(any("attempts" in w for w in report["warnings"]))

    def test_summary_one_line(self):
        with tempfile.TemporaryDirectory() as d:
            p = _write(Path(d))
            rc, out = self._run([str(p), "--summary"])
            self.assertEqual(rc, 0)
            self.assertIn("macro_phase=", out)
            self.assertEqual(out.count("\n"), 1)  # exactly one line


if __name__ == "__main__":
    unittest.main()
